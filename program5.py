import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("File Path")

# Scatter Plot
plt.scatter(df["sepal_length"], df["petal_length"])
plt.title("Scatter Plot")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

# Bar Chart
df["species"].value_counts().plot(kind="bar")
plt.title("Bar Chart")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()
