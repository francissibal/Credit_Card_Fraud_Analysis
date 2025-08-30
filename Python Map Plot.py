import pandas as pd
import plotly.express as px

# --- 1. Load Data from CSV ---
try:
    df = pd.read_csv("ccf_data.csv")
    print("CSV loaded successfully.")
    print(df.head())
except Exception as e:
    print(f"Error loading CSV: {e}")
    exit()

# --- 2. Fraud Analysis by State ---
print("Calculating fraud rates by state...")

df_state_fraud = (
    df.groupby("state")
    .agg(
        total_transactions=("state", "count"),
        fraudulent_transactions=("is_fraud", "sum")
    )
    .reset_index()
)

df_state_fraud["fraud_rate_percent"] = (
    df_state_fraud["fraudulent_transactions"] / df_state_fraud["total_transactions"] * 100
)

print("Data aggregated successfully.")
print(df_state_fraud.head())

# --- 3. Create Visualization ---
print("Generating choropleth map...")

fig = px.choropleth(
    df_state_fraud,
    locations='state',                # Column with state abbreviations
    locationmode="USA-states",        # Plot US states
    color='fraud_rate_percent',       # Fraud rate drives color intensity
    scope="usa",                      # Focus map on the USA
    hover_name='state',               # Show state name on hover
    hover_data={                      # Additional data on hover
        'fraud_rate_percent': ':.2f',
        'fraudulent_transactions': True,
        'total_transactions': True
    },
    color_continuous_scale="Reds",
    title="Credit Card Fraud Rate by State (%)"
)

fig.update_layout(
    title_x=0.5,
    geo=dict(
        lakecolor='rgb(255, 255, 255)'
    )
)

# --- 4. Save the Map ---
output_filename = "fraud_rate_by_state_map.html"
fig.write_html(output_filename)

print(f"\nInteractive map saved successfully as '{output_filename}'")
print("Open this file in your web browser to view the map.")
