# COVID-19 Global Data Tracker
# Author: Duale
# Description: Analyze and visualize global COVID-19 trends using real-time data

import pandas as pd
import plotly.express as px
import requests

# Load COVID-19 data from a live API
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

try:
    df = pd.read_csv(url)
    print("✅ Data loaded successfully!")
except Exception as e:
    print("❌ Failed to load data:", e)

# Preview dataset
df.head()
# Check for missing values
missing_data = df.isnull().sum().sort_values(ascending=False)
missing_data.head(10)
# Drop irrelevant or highly null columns
df_cleaned = df.drop(columns=['iso_code', 'continent', 'tests_units'], errors='ignore')
df_cleaned = df_cleaned.dropna(subset=["location", "total_cases", "total_deaths"])

# Filter for latest data
latest_data = df_cleaned[df_cleaned["date"] == df_cleaned["date"].max()]
latest_data = latest_data.sort_values(by="total_cases", ascending=False).head(20)

# View cleaned data
latest_data[["location", "total_cases", "total_deaths", "population"]]
# Bar chart - Top 20 Countries by Total Cases
fig = px.bar(
    latest_data,
    x="location",
    y="total_cases",
    color="location",
    title="Top 20 Countries by Total COVID-19 Cases",
    labels={"total_cases": "Total Cases", "location": "Country"},
    template="plotly_dark"
)
fig.show()
# Calculate case fatality rate
latest_data["fatality_rate (%)"] = (latest_data["total_deaths"] / latest_data["total_cases"]) * 100

# Display top 10 countries by fatality rate
fatalities = latest_data.sort_values(by="fatality_rate (%)", ascending=False)
fatalities[["location", "fatality_rate (%)"]].head(10)
# Line Chart: Trend of COVID-19 in a specific country (e.g., Kenya)
kenya = df[df["location"] == "Kenya"]

fig = px.line(
    kenya,
    x="date",
    y="total_cases",
    title="COVID-19 Trend in Kenya",
    labels={"total_cases": "Total Cases"},
    template="plotly_white"
)
fig.show()
# Scatter plot: Population vs Total Cases (latest)
fig = px.scatter(
    latest_data,
    x="population",
    y="total_cases",
    color="location",
    size="total_deaths",
    title="Population vs Total COVID-19 Cases",
    labels={"population": "Population", "total_cases": "Total Cases"},
    template="plotly_dark"
)
fig.show()
# Insights
print("🔍 Insights:")
print(f"📌 The country with the highest total cases: {latest_data.iloc[0]['location']}")
print(f"📌 The highest fatality rate is in: {fatalities.iloc[0]['location']} ({fatalities.iloc[0]['fatality_rate (%)']:.2f}%)")
print("📈 Kenya's data shows a gradual rise in cases over time.")
