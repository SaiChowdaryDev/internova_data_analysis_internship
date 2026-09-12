# Superstore Sales & Profit Analysis

## Project Overview

This project is a complete Data Analytics project based on the **Superstore Sales dataset**.

The project covers the complete analytics process, starting from data preparation and exploratory data analysis to data visualization and an interactive Power BI dashboard.

The main objective is to understand sales, profit, customer orders, product performance, regional performance, and the relationship between discounts and profit.

---

## Problem Statement

Businesses need to understand their sales and profit performance to make better decisions.

This project analyzes the Superstore dataset to identify:

* Sales and profit performance
* Best and low-performing categories
* Regional sales performance
* Sub-category profitability
* Relationship between discount and profit
* Important business trends and patterns

The analysis provides data-driven insights and recommendations that can help improve business performance.

---

## Dataset Description

The dataset used for this project is the **Superstore Sales dataset**.

### Dataset Size

* **Rows:** 10,194
* **Columns:** 21
* **Missing Values:** 0
* **Duplicate Rows:** 0

### Important Columns

* Order ID
* Order Date
* Ship Date
* Ship Mode
* Customer ID
* Customer Name
* Segment
* Country/Region
* City
* State/Province
* Region
* Product ID
* Category
* Sub-Category
* Product Name
* Sales
* Quantity
* Discount
* Profit

---

## Tools & Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Power BI
* Git
* GitHub
* Jupyter Notebook / Google Colab

---

## Data Preparation & Cleaning

The dataset was inspected and prepared before analysis.

### Data Quality Checks

* Checked dataset shape and column names
* Checked data types
* Checked missing values
* Checked duplicate records
* Checked negative sales values
* Checked negative profit values
* Checked outliers

### Results

* No missing values were found.
* No duplicate rows were found.
* No negative sales values were found.
* Negative profit values were retained because they represent genuine loss-making transactions.
* Outliers were identified but not automatically removed because extreme values can represent valid business transactions.

The cleaned dataset was exported as:

`cleaned_superstore_data.csv`

---

## Exploratory Data Analysis

Descriptive statistics were calculated for:

* Sales
* Quantity
* Discount
* Profit

### Overall Business Metrics

* **Total Sales:** 2,326,534.35
* **Total Profit:** 292,296.81
* **Total Quantity:** 38,654
* **Total Orders:** 5,111
* **Total Customers:** 804

### Correlation Analysis

Important correlations identified:

* **Sales & Profit:** 0.481
* **Discount & Profit:** -0.219
* **Quantity & Profit:** 0.066
* **Sales & Quantity:** 0.198

Sales and Profit showed a moderate positive relationship.

Discount and Profit showed a negative relationship, meaning higher discounts were generally associated with lower profit in this dataset.

Correlation shows association and does not by itself prove causation.

---

## Outlier Analysis

The IQR method was used to identify unusual values.

Outliers were found in:

* Sales
* Quantity
* Discount
* Profit

These values were retained because they may represent genuine high-value sales, large quantities, discounts, or profit/loss transactions.

---

## Data Visualizations

The following visualizations were created using Python:

1. **Sales by Category**
2. **Profit by Category**
3. **Sales by Region**
4. **Profit by Sub-Category**
5. **Discount vs Profit**
6. **Monthly Sales Trend**

These visualizations were used to identify patterns, comparisons, and business trends.

---

## Power BI Dashboard

An interactive Power BI dashboard was created to present the major business metrics and findings.

### KPI Cards

* Total Sales
* Total Profit
* Total Orders

### Dashboard Visualizations

* Sales by Category
* Profit by Category
* Sales by Region
* Profit by Sub-Category

### Interactive Filters

* Region
* Category
* Segment
* Ship Mode

The Power BI dashboard allows users to filter the data and analyze different parts of the business interactively.

---

## Key Insights

### 1. Technology Performance

Technology generated the highest overall sales and profit among the three main categories.

### 2. Furniture Profitability

Furniture generated significant sales, but its profit performance was comparatively lower than Technology.

This shows that higher sales do not always result in higher profitability.

### 3. Tables Performance

Tables were identified as a loss-making sub-category.

This area may require further investigation into pricing, discounts, and costs.

### 4. Discount and Profit

Discount and Profit had a negative correlation of **-0.219**.

This indicates that higher discounts were generally associated with lower profit in the analyzed data.

### 5. Sub-Category Performance

Copiers were among the strongest-performing sub-categories in terms of profit.

This makes them an important contributor to overall profitability.

---

## Business Recommendations

### 1. Optimize Discount Strategy

The business should review high-discount transactions and identify situations where discounts reduce profitability.

A more controlled discount strategy could help maintain sales while protecting profit margins.

### 2. Investigate Loss-Making Products

Loss-making sub-categories such as Tables should be analyzed further.

The business can review:

* Product pricing
* Discount levels
* Product costs
* Sales volume
* Customer demand

Based on this analysis, pricing or product-selection decisions can be improved.

---

## Conclusion

This project demonstrates an end-to-end data analytics workflow using the Superstore dataset.

The project included:

* Dataset inspection
* Data cleaning and preparation
* Exploratory Data Analysis
* Statistical analysis
* Correlation analysis
* Outlier analysis
* Data visualization
* Power BI dashboard development
* Business insights
* Data-driven recommendations

The analysis shows that understanding both **sales and profitability** is important for making better business decisions.

---

## Project Files

```text
Week-6 Data/
│
├── Sample-Superstore.csv.xls
├── cleaned_superstore_data.csv
│
├── Visualizations/
│   ├── sales_by_category.png
│   ├── profit_by_category.png
│   ├── sales_by_region.png
│   ├── profit_by_subcategory.png
│   ├── discount_vs_profit.png
│   └── monthly_sales_trend.png
│
├── PowerBI/
│   └── Superstore_Sales_Profit_Dashboard.pbix
│
└── README.md
```

---

## Author

**Sai Chowdary**

B.Tech CSE
Data Analytics Project — Internova Internship

