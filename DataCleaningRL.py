import pandas as pd

# Load the dataset
df = pd.read_csv("Análisis de datos/mission_launches.csv")

# DATA CLEANING

# Identify missing values
ValoresNulos = df.isnull().sum()
print(ValoresNulos)

# Replace missing values in the 'Price' column with the mean price
df["Price"] = df["Price"].fillna(df["Price"].mean())
print(df.tail())

# Note: The commented-out code below can be used to check for empty strings, spaces, or specific values that may indicate missing data.
# Uncomment these if additional cleaning is required.

# Count empty strings or spaces
# print((df == '').sum())
# print((df == ' ').sum())

# Count specific values that might be considered as null (e.g., 'N/A', 'none')
# print((df == 'N/A').sum())
# print((df == 'none').sum())

# Remove unnecessary columns
df = df.drop(df.columns[[0, 1]], axis=1)
print(df.head())

# Verify data types
print(df.dtypes)

# Change data type of the 'Price' column

# Display unique values and their counts in the 'Price' column
print(df['Price'].value_counts(dropna=False))

# Display the current data type of the 'Price' column
print(df['Price'].dtype)

# Convert the 'Price' column to a numeric type, coercing errors to NaN
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
print("Values after forced conversion:", df['Price'].value_counts(dropna=False))

# Optional: fill NaN values with 0 and convert to integer
df['Price'] = df['Price'].fillna(0).astype(int)

# Convert 'Date' column to datetime format (data cleaning)
df['Date'] = pd.to_datetime(df['Date'], format='%a %b %d, %Y %H:%M %Z', errors='coerce')

# Extract the year from the 'Date' column
df["Year"] = df["Date"].dt.year

# Extract the month from the 'Date' column
df["Month"] = df["Date"].dt.month

# Display data types after cleaning and transformation
print(df.dtypes)

# Save the cleaned data to a new CSV file
df.to_csv("Análisis de datos/mission_launches_clean2.csv", index=False)
