import numpy as np
import pandas as pd

a1 = { "ONE": pd.Series([1, 4, 5, 5], index=["a", "b", "c", "d"]), "TWO": pd.Series([1, 2, 6], index=["a", "b", "c"]) }
df1 = pd.DataFrame(a1)
print(df1)
print(df1["ONE"])
df1['THREE'] = df1["ONE"] * df1["TWO"] # Creates a new column
df1["FLAG"] = df1["THREE"] > 15
print(df1)
del df1["TWO"]
# del df1["one"] # Raises a KeyError
flags = df1.pop("FLAG")
# flags = df1.pop("FLAGS") # Raises a KeyError
print(flags)
df1["FOO"] = "BAR" # Scalar fills all values
df1["ONE_TRUNC"] = df1["ONE"][:2]
df1.insert(1, "ONE COPY", df1["ONE"])
print(df1)

iris = pd.read_csv("iris.csv")
print(iris.head())
# Ways to do it
# iris["sepalratio"] = iris["sepalwidth"] / iris["sepallength"]
# iris = iris.assign(sepalratio=iris["sepalwidth"] / iris["sepallength"])
iris = iris.assign(sepalratio=lambda x: (x["sepalwidth"] / x["sepallength"]))
iris = iris.assign(petalratio=lambda x: (x["petalwidth"] / x["petallength"]))
print(iris.head())

# Will work on Jupyter but not on VS Code as far as I know
# iris.query("sepallength > 5").plot(kind="scatter", x="sepalratio", y="petalratio")