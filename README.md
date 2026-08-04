# E-commerce Sales Analysis

An end-to-end data analysis project focused on e-commerce sales performance. The project demonstrates the complete analytical workflow, starting from SQL data extraction, through Python-based analysis, and ending with an interactive Power BI dashboard.

---

## Project Overview

The objective of this project was to analyze sales data from an e-commerce company in order to identify sales trends, best-selling products, customer behavior, and key business insights.

The project covers the entire data analysis process:

- Data extraction using SQL
- Data processing and analysis using Python
- Data visualization using Matplotlib
- Interactive dashboard creation using Microsoft Power BI

---

## Technologies

- MySQL
- SQL
- Python
- Pandas
- NumPy
- Matplotlib
- Microsoft Power BI
- Git

---

## Dataset

The analysis is based on an e-commerce relational database containing information about:

- Customers
- Orders
- Order Details
- Products
- Product Categories
- Payments
- Offices
- Employees

---

## Project Structure

```
ecommerce-sales-analysis/
│
├── database/
│   ├── database.sql
│   ├── queries.sql
│
├── data/
│   ├── customers.csv
│   ├── orders.csv
│   ├── orderdetails.csv
│   ├── products.csv
│   ├── productlines.csv
│   └── ...
│
├── python/
│   ├── analysis.py
│   └── requirements.txt
│
├── powerbi/
│   └── ecommerce_dashboard.pbix
│
├── charts/
│   ├── categories_revenue.py
│   ├── monthly_revenue.py
|   └── top_products.pdf
│
├── report/
│   └── Ecommerce_Sales_Report.pdf
│
└── README.md
```

---

## SQL Analysis

SQL was used to prepare and analyze data.

Example analyses include:

- Total revenue
- Revenue by month
- Revenue by product category
- Top-selling products
- Top customers
- Average order value
- Order status analysis
- Customer purchase analysis

---

## Python Analysis

Python was used to perform additional data processing and create visualizations.

Implemented analyses include:

- Monthly revenue trends
- Revenue by product category
- Top 10 products
- Top customers
- Sales distribution
- Revenue calculations
- Business insights

Libraries used:

- Pandas
- NumPy
- Matplotlib
- mysql-connector-python

---

## Power BI Dashboard

The dashboard provides an interactive overview of sales performance.

### KPIs

- Total Revenue
- Orders Count
- Products Sold
- Average Order Value

### Visualizations

- Revenue by Month
- Top 10 Products by Revenue
- Revenue by Product Category
- Order Status Distribution
- Top Customers by Revenue

### Interactive Filters

- Country
- Product Category
- Date

---

## Business Insights

The analysis revealed several key insights:

- Classic Cars generated the highest revenue among all product categories.
- A small number of customers account for a significant share of total revenue.
- Revenue follows seasonal trends, with noticeable peaks during certain months.
- Product categories contribute differently to overall sales performance.
- Most orders were successfully shipped, with only a small percentage cancelled or disputed.

---

## Dashboard Preview

<img width="1441" height="809" alt="image" src="https://github.com/user-attachments/assets/60343800-eeba-4dcb-b020-c39badec8961" />

## How to Run

### Install required libraries

```bash
pip install -r python/requirements.txt
```

### Run the analysis

```bash
python python/analysis.py
```

---

## Repository Contents

- SQL scripts for database analysis
- Python scripts for data processing
- Power BI dashboard
- Project report (PDF)
- Charts generated during analysis

---

## Author

**Wojciech Sojka**

Junior Data Analyst Portfolio Project
