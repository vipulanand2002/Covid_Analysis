import pandas as pd
import matplotlib.pyplot as plt

df_filtered = pd.read_csv("../cleaned_covid_data.csv")

# Get latest available data
latest_date = df_filtered["date"].max()
df_latest = df_filtered[df_filtered["date"] == latest_date]

# Select top 10 countries by total cases (excluding 'World' and continents)
top_countries = df_latest[~df_latest["location"].isin(["World", "Europe", "Asia", "Africa", "North America", "South America", "Oceania"])]
top_countries = top_countries.nlargest(10, "total_cases")

# Bar plot
plt.figure(figsize=(12, 6))
plt.barh(top_countries["location"], top_countries["total_cases"], color="purple")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.title("Top 10 Countries with the Highest COVID-19 Cases")
plt.gca().invert_yaxis()  # Invert order to show highest first
plt.show()
