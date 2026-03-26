#!/usr/bin/env python
# coding: utf-8

# ## Streamlit Dashboard

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Retail Analytics Dashboard", layout="wide")

# ================================
# ✅ LOAD DATA ONLY ONCE (CACHED)
# ================================
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_data.csv")
    rfm = pd.read_csv("data/rfm_data.csv")
    raw_df = pd.read_csv("data/raw_data.csv")

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Category function inside cache
    def get_category(desc):
        desc = str(desc).upper()
        if "SET" in desc: return "Sets"
        elif "BAG" in desc: return "Bags & Packaging"
        elif "BOX" in desc: return "Storage"
        elif "HEART" in desc: return "Home Decor"
        elif "LIGHT" in desc: return "Lighting"
        elif "CAKE" in desc: return "Kitchenware"
        elif "TOY" in desc: return "Toys & Games"
        elif "PARTY" in desc: return "Party Supplies"
        elif "PAPER" in desc: return "Craft Supplies"
        else: return "Other"

    df["Category"] = df["Description"].apply(get_category)

    return df, rfm, raw_df

# LOAD ONCE
df, rfm, raw_df = load_data()

# ================================
# SIDEBAR NAVIGATION
# ================================
page = st.sidebar.radio("📌 Navigation", ["Business Overview", "Customer RFM Analysis"])

# ============================================
# 🏠 PAGE 1: BUSINESS OVERVIEW
# ============================================
if page == "Business Overview":

    st.title("📊 Business Overview Dashboard")

    # KPIs
    total_revenue = df["Revenue"].sum()
    total_customers = df["CustomerID"].nunique()
    total_orders = df["InvoiceNo"].nunique()
    AOV = total_revenue / total_orders

    # Return rate (from raw)
    total_orders_raw = raw_df["InvoiceNo"].nunique()
    cancelled_orders = raw_df[raw_df["InvoiceNo"].astype(str).str.startswith("C")]["InvoiceNo"].nunique()
    return_rate = (cancelled_orders / total_orders_raw) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Revenue", f"${total_revenue:,.0f}")
    col2.metric("👥 Customers", total_customers)
    col3.metric("🛒 AOV", f"${AOV:.2f}")
    col4.metric("🔁 Return Rate", f"{return_rate:.2f}%")

    st.markdown("---")

    # ================================
    # 📅 REVENUE TRENDS
    # ================================
    st.subheader("📅 Revenue Trends")

    col1, col2 = st.columns(2)

    df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    monthly = df.groupby("YearMonth")["Revenue"].sum().reset_index()

    fig1 = px.line(monthly, x="YearMonth", y="Revenue", title="Monthly Revenue Trend")
    fig1.update_traces(line=dict(width=3))
    fig1.update_layout(template="plotly_dark")

    col1.plotly_chart(fig1, use_container_width=True)

    df["Date"] = df["InvoiceDate"].dt.date
    daily = df.groupby("Date")["Revenue"].sum().reset_index()

    fig2 = px.line(daily, x="Date", y="Revenue", title="Daily Revenue Trend")
    fig2.update_traces(line=dict(color="green"))
    fig2.update_layout(template="plotly_dark")

    col2.plotly_chart(fig2, use_container_width=True)

    # ================================
    # 🌍 GEOGRAPHIC ANALYSIS
    # ================================
    st.subheader("🌍 Geographic Analysis")

    col1, col2 = st.columns(2)

    country = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10).reset_index()

    fig3 = px.bar(
        country,
        x="Revenue",
        y="Country",
        orientation="h",
        title="Top 10 Countries by Revenue"
    )
    fig3.update_layout(template="plotly_dark")

    col1.plotly_chart(fig3, use_container_width=True)

    fig4 = px.pie(
        country,
        names="Country",
        values="Revenue",
        title="Revenue Distribution"
    )
    fig4.update_layout(template="plotly_dark")

    col2.plotly_chart(fig4, use_container_width=True)

    # ================================
    # 🛍️ PRODUCT PERFORMANCE
    # ================================
    st.subheader("🛍️ Product Performance")

    col1, col2 = st.columns(2)

    top_products = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(15).reset_index()

    fig5 = px.bar(
        top_products,
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top 15 Products by Revenue"
    )
    fig5.update_layout(template="plotly_dark")

    col1.plotly_chart(fig5, use_container_width=True)

    top_cat = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False).head(10).reset_index()

    fig6 = px.bar(
        top_cat,
        x="Revenue",
        y="Category",
        orientation="h",
        title="Top Categories by Revenue"
    )
    fig6.update_layout(template="plotly_dark")

    col2.plotly_chart(fig6, use_container_width=True)

# ============================================
# 👤 PAGE 2: CUSTOMER RFM ANALYSIS
# ============================================
else:

    st.title("👤 Customer RFM Analysis")

    customer_id = st.selectbox("Select Customer ID", sorted(rfm["CustomerID"].unique()))

    customer = rfm[rfm["CustomerID"] == customer_id].iloc[0]
    customer_txn = df[df["CustomerID"] == customer_id]

    st.subheader("Customer Profile")

    col1, col2, col3 = st.columns(3)

    col1.metric("Segment", customer["Segment"])
    col2.metric("Total Spend", f"${customer['Monetary']:.2f}")
    col3.metric("Transactions", int(customer["Frequency"]))

    st.write(f"📅 First Purchase: {customer_txn['InvoiceDate'].min()}")
    st.write(f"📅 Last Purchase: {customer_txn['InvoiceDate'].max()}")
    st.write(f"🌍 Country: {customer_txn['Country'].mode()[0]}")

    st.subheader("🎯 Recommendation")

    segment = customer["Segment"]

    if segment == "Champions":
        st.success("Reward with VIP offers and exclusive deals.")
    elif segment == "Loyal Customers":
        st.info("Upsell premium products and memberships.")
    elif segment == "At Risk":
        st.warning("Send discounts and win-back campaigns.")
    elif segment == "New Customers":
        st.info("Provide onboarding offers.")
    else:
        st.write("Engage with general promotions.")

    st.subheader("Top Products Purchased")

    top_products = (
        customer_txn.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig7 = px.bar(top_products, x="Description", y="Revenue", title="Top Products")
    fig7.update_layout(template="plotly_dark")

    st.plotly_chart(fig7, use_container_width=True)

    st.subheader("Category Distribution")

    customer_txn["Category"] = customer_txn["Description"].apply(
        lambda x: "Sets" if "SET" in str(x).upper() else "Other"
    )

    cat = customer_txn.groupby("Category")["Revenue"].sum().reset_index()

    fig8 = px.pie(cat, names="Category", values="Revenue")
    fig8.update_layout(template="plotly_dark")

    st.plotly_chart(fig8, use_container_width=True)

