# A DataFrame is a 2-dimensional labeled data structure with columns of potentially diff types
# A dict of Series objects
# Like a spreadsheet or SQL table
# Accepts:
# - Dict of 1D ndarrays, lists, dicts, or Series
# - 2D numpy.ndarray
# - Structured or record ndarray
# - A Series
# - Another DataFrame

import pandas as pd
import numpy as np
from collections import namedtuple
from dataclasses import make_dataclass

a1 = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df1 = pd.DataFrame(a1)
df2 = pd.DataFrame(a1, index=["d", "c", "a"])
df3 = pd.DataFrame(a1, index=["a", "b", "a"], columns=["one", "three"])
print(df1)
print(df3)
print(df3.index, df3.columns)
a2 = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")])
print(a2)
a2[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]
df4 = pd.DataFrame(a2, index=["first", "second"])
print(df4)

# Can create a MultiIndex DataFrame from a dict of tuples
b1 = pd.DataFrame({
                ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
                ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
                ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
                ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
                ("b", "b"): {("A", "D"): 9, ("A", "B"): 10},
            })
print(b1)

# Can create DataFrame from a list of namedtuples
Point = namedtuple("Point", "x y")
c1 = pd.DataFrame([Point(0, 0), Point(0, 3), (2, 3)])
print(c1)

# Can create DataFrame from a list of dataclasses, equivalent to passing a list of dictionaries
Point2 = make_dataclass("Point2", [("x", int), ("y", int)])
d1 = pd.DataFrame([Point2(0, 0), Point2(0, 3), Point2(2, 3)])
print(d1)

# Can use alternate constructors
e1 = dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]) # {'A': [1, 2, 3], 'B': [4, 5, 6]}
e2 = pd.DataFrame.from_dict(e1)
print(e2)
e3 = pd.DataFrame.from_dict(e1, orient='index', columns=["test1", "test2", "test3"])
print(e3)
e4 = np.array([(1, 2, "Hello"), (5, 4, "World")], dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")])
e5 = pd.DataFrame.from_records(e4, index="C")
print(e5)