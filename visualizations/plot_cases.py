import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df_filtered = pd.read_csv("../cleaned_covid_data.csv")

# Filter for worldwide data
df_global = df_filtered[df_filtered["location"] == "World"]

# Plot total cases over time
plt.figure(figsize=(12, 6))
plt.plot(df_global["date"], df_global["total_cases"], label="Total Cases", color="blue")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("Global COVID-19 Cases Over Time")
plt.legend()
plt.grid(True)
plt.show()