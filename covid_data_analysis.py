import pandas as pd

#Step: 1 - Load the dataset from URL for COVID-19 data
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


#Step: 2 - Data Preprocessing

# Handling the Missing Values
missing_values = df.isnull().sum()
print("\nMissing Values Count:")
print(missing_values[missing_values > 0])

# Filtering only necessary data
df_filtered = df[['date', 'location', 'continent', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_tests','new_tests', 'total_vaccinations', 'people_vaccinated' , 'gdp_per_capita', 'population']]

# Convert 'date' column to datetime format safely
df_filtered.loc[:, 'date'] = pd.to_datetime(df_filtered['date'])

# Remove duplicates safely
df_filtered = df_filtered.drop_duplicates().copy()