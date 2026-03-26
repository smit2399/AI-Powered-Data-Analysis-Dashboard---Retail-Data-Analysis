# 📊 AI-Powered Retail Analytics Dashboard

## 🚀 Project Overview

This project is an end-to-end data analytics solution built on an e-commerce retail dataset. It transforms raw transactional data into actionable business insights using data analysis, customer segmentation (RFM), and an interactive Streamlit dashboard.

The dashboard enables stakeholders to:

- Monitor revenue and sales trends
- Analyze geographic and product performance
- Understand customer behavior using RFM segmentation
- Make data-driven business decisions

---

## 🎯 Key Features

### 📌 Business Overview Dashboard
- 💰 Total Revenue, Customers, AOV, Return Rate
- 📈 Revenue Trends (Monthly & Daily)
- 🌍 Geographic Analysis (Top countries, distribution)
- 🛍️ Product Performance (Top products & categories)

---

### 👤 Customer RFM Analysis
- Customer segmentation into 7 groups:
	- Champions
	- Loyal Customers
	- New Customers
	- Potential Loyalists
	- At Risk
	- Hibernating
	- Others
- Customer lookup (dropdown selector)
- Personalized recommendations
- Customer profile:
	- Purchase history
	- Total spend
	- Transaction count
- Product & category insights per customer

---

## 🧠 Business Value

This project provides insights into:

- 📊 Revenue drivers and seasonal trends
- 🌍 Market dependency and geographic opportunities
- 🛍️ High-performing products and categories
- 👥 Customer segmentation and lifetime value
- ⚠️ Churn detection and retention strategies

---

## 📂 Project Structure

retail-dashboard/
│
├── app.py
├── requirements.txt
├── data/
│   ├── cleaned_data.csv
│   ├── rfm_data.csv
│   └── raw_data.csv
│
├── notebooks/
│   ├── retail_data_analysis.ipynb
│   └── RFM_analysis.ipynb

---

## ⚙️ Tech Stack
- Python
- Pandas / NumPy → Data processing
- Matplotlib / Seaborn / Plotly → Visualization
- Streamlit → Interactive dashboard
- Git & GitHub → Version control

---

## 📊 Data Pipeline

**1. Data Cleaning**
	- Removed duplicates and null values
	- Handled returns and cancellations
	- Created **Revenue** column

**2. Exploratory Data Analysis**
Revenue trends
Product and geographic insights

**3. Feature Engineering**
Time features (Month, Day, Hour)
Product categories

**4. RFM Segmentation**
Recency, Frequency, Monetary calculation
Customer scoring and segmentation

**5. Dashboard Development**
Interactive 2-page Streamlit app

---

## 📈 Key Insights

- Revenue is highly seasonal, peaking in Nov–Dec
- Business is heavily dependent on UK market
- A small percentage of customers contribute majority of revenue
- Product performance follows the Pareto principle (80/20 rule)
- Most orders are low value, indicating opportunity to increase AOV

---

## 🚀 Deployment

The app is deployed using Streamlit Cloud.

### 🔗 Live Demo

👉 Add your deployed app link here

---

## 🛠️ Installation & Setup

**1️. Clone the repository**

- git clone https://github.com/YOUR_USERNAME/AI-Powered-Data-Analysis-Dashboard---Retail-Data-Analysis.git
- cd AI-Powered-Data-Analysis-Dashboard---Retail-Data-Analysis

**2️. Create virtual environment**

- python -m venv venv
- venv\Scripts\activate

**3️. Install dependencies**

- pip install -r requirements.txt

**4️. Run the app**

- streamlit run app.py

---

## 📦 Requirements

streamlit
pandas
plotly
openpyxl

---

## 🔥 Future Enhancements

- 🔍 Add filters (date, country, segment)
- 🤖 Churn prediction model (ML)
- 🎯 Recommendation system (category-based)
- 💎 Advanced UI (cards, animations)
- 📊 Real-time data integration

---

## 🧠 What I Learned

- Building end-to-end data analytics solutions
- Translating data into business insights
- Designing interactive dashboards
- Customer segmentation using RFM
- Deploying production-ready apps

---

##👨‍💻 Author

**Smit Prajapati**

- Data Enthusiast | Analytics | Machine Learning
- Passionate about building data-driven solutions

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to connect!

---