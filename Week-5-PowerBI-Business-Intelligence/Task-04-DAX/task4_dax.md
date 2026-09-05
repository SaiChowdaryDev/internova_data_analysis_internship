# Task 4 - DAX Calculated Columns & Measures

## Objective

To create DAX measures for calculating important business metrics.

## DAX Measures

- Total Sales = SUM(Sales[Sales])
- Total Orders = DISTINCTCOUNT(Sales[Order_ID])
- Average Order Value = DIVIDE([Total Sales], [Total Orders])
- Maximum Sale = MAX(Sales[Sales])
- Minimum Sale = MIN(Sales[Sales])

## Results

- Total Sales: 25,860
- Total Orders: 20
- Average Order Value: 1,293
- Maximum Sale: 2,550
- Minimum Sale: 300

## Conclusion

DAX measures were created successfully to calculate sales performance and order-related metrics in Power BI.
