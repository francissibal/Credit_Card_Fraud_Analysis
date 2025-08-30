Credit Card Fraud Detection Analysis (2019-2020)
This repository contains the end-to-end analysis of a credit card transaction dataset to identify and predict instances of fraud. The project involves exploratory data analysis using SQL, Python and Microsoft Power BI.

Project Overview & Objective
A new credit card company in the western United States wants to establish itself as a market leader in security. The primary objective is to build a predictive model that can accurately identify fraudulent transactions from a provided dataset. A key requirement is that the model should prioritize catching as many fraudulent cases as possible (high recall), even if it means occasionally flagging a legitimate transaction for review.

Visualizations & Key Dashboards
Below are some of the key visualizations in Microsoft Power BI. These charts highlight the primary findings from the exploratory data analysis phase.


# SQL Portfolio

## Question 1  
Return the age, total official points, and number of tournaments played for the top 5 tennis players in the world.

📄 [View the SQL query](./Query 1.sql)

```sql
-- Query 1: What types of purchases are most likely to be instances of fraud?
-- It analyzes fraud rates and average transaction amounts by merchant category.

WITH FraudStats AS (
    SELECT
        category,
        COUNT(*) AS total_transactions,
        SUM(is_fraud) AS fraudulent_transactions,
        AVG(CASE WHEN is_fraud = 1 THEN amt ELSE NULL END) as avg_fraud_amount,
        AVG(CASE WHEN is_fraud = 0 THEN amt ELSE NULL END) as avg_legit_amount
    FROM
        transactions
    GROUP BY
        category
)
SELECT
    category,
    total_transactions,
    fraudulent_transactions,
    (fraudulent_transactions * 1.0 / total_transactions) * 100 AS fraud_rate_percent,
    avg_fraud_amount,
    avg_legit_amount
FROM
    FraudStats
ORDER BY
    fraud_rate_percent DESC;

