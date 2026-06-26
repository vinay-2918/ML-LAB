import pandas as pd
from sklearn.datasets import load_iris
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.DataFrame(load_iris().data)

# Create a missing value
df.iloc[0,0] = None

# Fill missing value
df = pd.DataFrame(SimpleImputer().fit_transform(df))

# Scale the data
df = pd.DataFrame(StandardScaler().fit_transform(df))

print(df.head())
