"""
CleanAir India - Beginner Data Analytics Project

Libraries used: NumPy and Pandas only.
IMPORTANT: The included CSV contains illustrative demo values only.
Replace it with verified CPCB / data.gov.in data before making
real-world claims.
"""

import numpy as np
import pandas as pd

# 1. Load data
DATA_FILE = "data/air_quality_demo.csv"

df = pd.read_csv(DATA_FILE)

# 2. Basic data checks and cleaning
df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")
df = df.dropna(subset=["City", "Month", "AQI"])

# Keep only valid, finite, non-negative AQI values
df = df[np.isfinite(df["AQI"])]
df = df[df["AQI"] >= 0]

print("\n--- DATA PREVIEW ---")
print(df.head(10))

print("\n--- DATA SUMMARY ---")
print(df.describe())

# 3. City-wise average AQI
city_avg = (
    df.groupby("City", as_index=False)["AQI"]
      .mean()
      .sort_values("AQI", ascending=False)
)

print("\n--- CITY-WISE AVERAGE AQI ---")
print(city_avg.round(1).to_string(index=False))
city_avg.to_csv("city_average_aqi.csv", index=False)

# 4. Find the highest average AQI city
highest_city = city_avg.iloc[0]
print(
    f"\nHighest average AQI in this dataset: "
    f"{highest_city['City']} ({highest_city['AQI']:.1f})"
)

# 5. Month-wise average AQI across all cities
month_avg = (
    df.groupby(["Month_Number", "Month"], as_index=False)["AQI"]
      .mean()
      .sort_values("Month_Number")
)

print("\n--- MONTH-WISE AVERAGE AQI ---")
print(month_avg[["Month", "AQI"]].round(1).to_string(index=False))
month_avg.to_csv("month_average_aqi.csv", index=False)

# 6. Save cleaned data
df.to_csv("cleaned_air_quality_data.csv", index=False)

print("\nAnalysis completed successfully.")
print("CSV reports saved in the current project folder.")
print("\nReminder: Demo data is not official or suitable for factual conclusions.")
