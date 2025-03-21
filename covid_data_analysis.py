import pandas as pd

# Load dataset from URL
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Display basic information
print("\nDataset Information:")
print(df.info())

# Show first 5 rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check dataset columns
print("\nColumn Names:")
print(df.columns)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values Count:")
print(df.isnull().sum())
