# Credit Card Fraud Detection Analysis (2019-2020)
This repository contains the end-to-end analysis of a credit card transaction dataset to identify and predict instances of fraud. The project involves exploratory data analysis using SQL, Python and Microsoft Power BI.

## Project Overview & Objective
A new credit card company in the western United States wants to establish itself as a market leader in security. The primary objective is to build a predictive model that can accurately identify fraudulent transactions from a provided dataset. A key requirement is that the model should prioritize catching as many fraudulent cases as possible (high recall), even if it means occasionally flagging a legitimate transaction for review.

## Visualizations & Key Dashboards
Below are some of the key visualizations. These charts highlight the primary findings from the exploratory data analysis phase.

## Microsoft Power BI Dashboard:
### Main Dashboard:

![PowerBIPreview1](CreditCardFraud-Dashboard-1.png)

## Data Analysis & Key Insights
This analysis covers 1,782 fraudulent transactions totaling $923.19K from 2019-2020, representing an overall fraud rate of 0.52%.

## Demographic and Category Insights
Most Affected Age Group: Older customers are the primary targets. The 46-60 age group is the most affected (569 transactions), followed closely by the 61+ group (540 transactions).

Top Risk Categories: Online shopping (shopping_net) has the highest fraud rate at 1.44%. This is followed by in-person grocery (grocery_pos) at 1.32% and miscellaneous online transactions (misc_net) at 1.28%.

## Geographic and Merchant Hotspots
Top State by Fraud Amount: California leads all states in total fraudulent losses with $206K. Missouri ($131K) and Nebraska ($119K) follow.
Top State by Fraud Rate: While California has the highest total loss, Alaska (AK) has the highest proportional risk with a fraud rate of 1.69%.

### Drill through by State (Fraud Details):

![PowerBIPreview2](CreditCardFraud-Dashboard-1.png)

### Drill-Down on California: Within California (the state with the highest total fraud amount):

Top Cities: Glendale, San Diego, and San Jose are the top cities for the number of fraudulent incidents.

Top Merchant: The merchant "Romaguera, Cruickshank and Greenholt" experienced the highest fraud amount.

High-Risk Professions: Cardholders with the job title "Wellsite geologist" were the most targeted, followed by "Occupational therapist".

## Transactional Patterns
Monthly Trends: Fraudulent transactions fluctuate throughout the year, with a notable peak in March.

Behavioral Pattern: A common fraud signature was identified: transactions are typically for very low monetary amounts but occur at a significant physical distance from the legitimate cardholder's location, indicating card-not-present fraud.


## Question 1  
Returns the Top Category in Fradulent Rate %, Total Transactions, Total Fraud Transactions, Average of Fraud Amount and Legit Amount.

[View SQL File](Queries/Query1)

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
```

### ✅ Query 1 Result

| Category        | Total Transactions | Fraudulent Transactions  | Fraud Rate (%) | Avg Fraud Amount | Avg Legit Amount |
|-----------------|--------------------|--------------------------|----------------|------------------|------------------|
| shopping_net    | 26,379             | 381                      | 1.44           | 1,001.13         | 73.32            |
| grocery_pos     | 32,732             | 433                      | 1.32           | 315.23           | 122.07           |
| misc_net        | 16,898             | 217                      | 1.28           | 797.16           | 70.90            |
| shopping_pos    | 30,329             | 187                      | 0.62           | 886.33           | 74.94            |
| gas_transport   | 35,089             | 153                      | 0.44           | 12.65            | 62.96            |
| travel          | 10,322             | 33                       | 0.32           | 8.48             | 109.34           |
| misc_pos        | 20,024             | 62                       | 0.31           | 220.21           | 61.48            |
| grocery_net     | 11,355             | 27                       | 0.24           | 12.73            | 54.62            |
| entertainment   | 24,222             | 55                       | 0.23           | 535.51           | 62.45            |
| personal_care   | 24,406             | 55                       | 0.23           | 28.95            | 48.80            |
| kids_pets       | 29,704             | 55                       | 0.19           | 18.60            | 55.93            |
| food_dining     | 23,038             | 38                       | 0.16           | 117.27           | 50.56            |
| health_fitness  | 22,593             | 36                       | 0.16           | 20.33            | 54.22            |
| home            | 32,516             | 50                       | 0.15           | 261.47           | 56.75            |

## Question 2  
Returns the State, Total Transactions, Fraud Transactions, Fraud Rate (%).

[View SQL File](Queries/Query2)

```sql
-- Query 2: Fraud Analysis by State
-- Identifies geographic hotspots for fraudulent activity.
SELECT
    state,
    COUNT(*) as total_transactions,
    SUM(is_fraud) as fraudulent_transactions,
    (SUM(is_fraud) / COUNT(*)) * 100 as fraud_rate_percent
FROM
    transactions
GROUP BY
    state
ORDER BY
    fraud_rate_percent DESC;
```
### ✅ Query 2 Result
| State | Total Transactions | Fraudulent Transactions | Fraud Rate (%) |
|-------|--------------------|--------------------------|----------------|
| AK    | 2,963              | 50                       | 1.69           |
| OR    | 26,408             | 197                      | 0.75           |
| NE    | 34,425             | 216                      | 0.63           |
| CO    | 19,766             | 115                      | 0.58           |
| NM    | 23,427             | 121                      | 0.52           |
| CA    | 80,495             | 402                      | 0.50           |
| MO    | 54,904             | 262                      | 0.48           |
| WA    | 27,040             | 126                      | 0.47           |
| HI    | 3,649              | 16                       | 0.44           |
| WY    | 27,776             | 119                      | 0.43           |
| AZ    | 15,362             | 64                       | 0.42           |
| ID    | 8,035              | 33                       | 0.41           |
| UT    | 15,357             | 61                       | 0.40           |

## Question 3  
Returns the Age Group, Total Transactions, Fraud Transactions, Fraud Rate (%).
[View SQL File](Queries/Query3)
```sql
-- Query 3: Fraud Analysis by Age Group
-- Determines if certain age groups are more susceptible to fraud using the provided age column.
SELECT
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 60 THEN '46-60'
        WHEN age >= 61 THEN '61+'
        ELSE 'Under 18'
    END AS age_group,
    COUNT(*) as total_transactions,
    SUM(is_fraud) as fraudulent_transactions,
    (SUM(is_fraud) * 1.0 / COUNT(*)) * 100 as fraud_rate_percent
FROM
    transactions -- Use the 'transactions' table directly
GROUP BY
    age_group
ORDER BY
    age_group;
```
### ✅ Query 3 Result
| age_group | total_transactions | fraudulent_transactions | fraud_rate_percent |
|-----------|--------------------|--------------------------|--------------------|
| 18-25     | 17,622             | 149                      | 0.84553            |
| 26-35     | 73,100             | 283                      | 0.38714            |
| 36-45     | 68,678             | 241                      | 0.35091            |
| 46-60     | 101,763            | 569                      | 0.55914            |
| 61+       | 78,444             | 540                      | 0.68839            |







