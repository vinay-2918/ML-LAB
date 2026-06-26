import pandas as pd

# Load the dataset
df = pd.read_csv("iris.csv")      # Change the file name/path if needed

print("Dataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nUnique Species:")
print(df["species"].unique())
