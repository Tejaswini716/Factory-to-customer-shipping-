# 🚚 Factory-to-Customer Shipping Route Efficiency Analysis for Nassau Candy Distributor

## 📌 Project Overview

This project analyzes the shipping operations of **Nassau Candy Distributor** by evaluating factory-to-customer delivery routes across the United States. The objective is to identify efficient and inefficient shipping routes, detect regional bottlenecks, compare shipping modes, and provide actionable insights through an interactive **Streamlit Dashboard**.

The project combines **Data Cleaning, Exploratory Data Analysis (EDA), Feature Engineering, KPI Analysis, Geographic Visualization, and Business Intelligence** to support data-driven logistics optimization.

---

## 🎯 Problem Statement

Nassau Candy Distributor currently lacks visibility into:

- Efficient and inefficient factory-to-customer routes
- Shipping delays across different regions
- Geographic bottlenecks
- Ship mode performance
- Route-level operational efficiency

Without these insights, logistics optimization remains reactive rather than proactive.

---

## 🎯 Project Objectives

- Calculate Shipping Lead Time
- Analyze Factory → Customer shipping routes
- Measure route efficiency
- Compare shipping performance by ship mode
- Identify regional bottlenecks
- Build an interactive Streamlit dashboard
- Generate business recommendations for logistics optimization

---

# 🗂 Dataset Features

| Column | Description |
|---------|-------------|
| Row ID | Unique Row Identifier |
| Order ID | Order Identifier |
| Order Date | Order Placement Date |
| Ship Date | Shipment Date |
| Ship Mode | Shipping Method |
| Customer ID | Customer Identifier |
| Country/Region | Customer Country |
| City | Customer City |
| State/Province | Customer State |
| Postal Code | ZIP Code |
| Division | Product Division |
| Region | Customer Region |
| Product ID | Product Identifier |
| Product Name | Product Name |
| Sales | Sales Amount |
| Units | Quantity Sold |
| Gross Profit | Sales − Cost |
| Cost | Manufacturing Cost |

---

# 🏭 Factory Mapping

Products are mapped to manufacturing factories using the provided correlation table.

Example:

| Product | Factory |
|-----------|---------|
| Wonka Bar - Nutty Crunch Surprise | Lot's O' Nuts |
| Laffy Taffy | Sugar Shack |
| Wonka Gum | Secret Factory |
| Hair Toffee | The Other Factory |

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

# 📊 Project Workflow

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Route Definition
        │
        ▼
EDA
        │
        ▼
KPI Analysis
        │
        ▼
Visualization
        │
        ▼
Interactive Dashboard
```

---

# 🧹 Data Preprocessing

- Date Conversion
- Missing Value Handling
- Invalid Lead Time Removal
- Product → Factory Mapping
- Route Creation
- Delay Flag Generation

---

# ⚡ Feature Engineering

### Shipping Lead Time

```
Lead Time = Ship Date − Order Date
```

### Route

```
Factory → Customer State
```

Example:

```
Sugar Shack → Texas
```

### Delay Flag

```
Lead Time > Threshold
```

### Route Efficiency Score

Normalized inverse Lead Time using MinMaxScaler.

---

# 📈 Key Performance Indicators (KPIs)

- Average Shipping Lead Time
- Route Volume
- Delay Frequency
- Route Efficiency Score
- Lead Time Variability

---

# 📊 Exploratory Data Analysis

The project includes:

- Shipping Lead Time Distribution
- State-wise Analysis
- Region-wise Analysis
- Ship Mode Comparison
- Route Performance Analysis
- Monthly Shipping Trends
- Delay Frequency Analysis

---

# 🚚 Route Analysis

Each route is defined as:

```
Factory → Customer State
```

Metrics calculated:

- Total Shipments
- Average Lead Time
- Lead Time Standard Deviation
- Delay Percentage

---

# 🌎 Geographic Analysis

- US Shipping Heatmap
- State-wise Lead Time
- Regional Bottleneck Detection
- Shipment Density Analysis

---

# 🚛 Ship Mode Comparison

Performance comparison among:

- Standard Class
- Second Class
- First Class
- Same Day

Metrics:

- Average Lead Time
- Number of Orders
- Delivery Performance

---

# 💻 Streamlit Dashboard

## Dashboard Modules

### 📍 Route Efficiency Overview

- KPI Cards
- Average Lead Time
- Delay Frequency
- Top 10 Efficient Routes
- Bottom 10 Inefficient Routes

---

### 🗺 Geographic Shipping Map

- US Heatmap
- Regional Bottlenecks
- State-wise Performance

---

### 🚚 Ship Mode Comparison

- Ship Mode Performance
- Lead Time Distribution
- Cost vs Delivery Speed

---

### 🔍 Route Drill-Down

- State Selection
- Route Analysis
- Shipment Timeline
- Order-Level Details

---

# 🎛 Dashboard Filters

- Date Range
- Region
- State
- Ship Mode
- Lead Time Threshold

---

# 📂 Project Structure

```
Nassau_Candy_Project/

│
├── data/
│      Nassau_Candy.csv
│
├── notebooks/
│      EDA.ipynb
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│
└── report/
       Research_Paper.pdf
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Nassau-Candy-Shipping-Analysis.git
```

Move to project folder

```bash
cd Nassau-Candy-Shipping-Analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 📷 Dashboard Preview

Add screenshots here after deployment.

Example:

```
images/dashboard1.png

images/dashboard2.png

images/dashboard3.png
```

---

# 📈 Business Insights

- Identify fastest shipping routes
- Detect slow delivery regions
- Compare shipping methods
- Reduce operational delays
- Improve nationwide delivery performance
- Support data-driven logistics decisions

---

# 🚀 Future Improvements

- Machine Learning Lead Time Prediction
- Route Optimization Algorithms
- Weather Integration
- Real-Time Shipment Tracking
- Demand Forecasting
- Interactive Geographic Maps

---

# 📚 References

- Pandas Documentation
- Streamlit Documentation
- Plotly Documentation
- Scikit-learn Documentation

---

# 👩‍💻 Author

**Tejaswini Chowdhary**

B.Tech (Computer Science Engineering)

Data Analyst | Data Science Enthusiast

---

# ⭐ If you found this project useful, please give it a Star!
