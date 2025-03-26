import pandas as pd
import matplotlib.pyplot as plt

df_filtered = pd.read_csv("../cleaned_covid_data.csv")
df_global = df_filtered[df_filtered["location"] == "World"]

plt.figure(figsize=(12, 6))
plt.plot(df_global["date"], df_global["total_deaths"], label="Total Deaths", color="red")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.title("Global COVID-19 Deaths Over Time")
plt.legend()
plt.grid(True)
plt.show()
