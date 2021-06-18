import pandas as pd

iris_filename = "datasets/Iris.csv"
iris = pd.read_csv(iris_filename, sep=',', decimal='.', header=None,
        names=['sepal_length', 'sepal_width', 'petal_length', 'pedal_width', 'target'])

# Head (5 rows)
print("HEAD:\n", iris.head())

# Tail (last 5)
print("TAIL:\n", iris.tail())

# Dataset Columns
print("Columns:\n", iris.columns)

# Get "target" column
print("Column 'target'", iris["target"])
