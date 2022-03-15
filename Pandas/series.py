import numpy as np
import pandas as pd

a1 = pd.Series(np.random.randn(5))
print(a1)
# Index must be the same length as data
a2 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(a2)
print(a2.index)
a3 = { "test1": 5, "test2": 1, "test3": 8 }
a4 = pd.Series(a3)
a5 = pd.Series(a3, index=["test1", "test4", "test3"])
print(a4)
print(a5)
# Default length of 1, length determined by index property
a6 = pd.Series(5.0, index=["a", "b", "c"])
print(a6)
print(a6 + 2)
print(a2[:3])
print(a2[a2 > a2.median()])
print(a6.array) # Actual array backing a series
print(a6.to_numpy()) # Returns actual ndarray

# A series is like a fixed-size dict - you can get and set values by index
b1 = pd.Series(np.random.randn(8))
print(b1)
print(b1[0])
print(7 in b1)
b2 = pd.Series(np.random.randn(9), index=["a", "b", "c", "d", "e", "f", "g", "h", "i"])
print(b2)
print(b2["e"])
b2["f"] = 0.2
# print(b2["w"]) # KeyError will be raised
print(b2.get("w"))
print(b2 * 2)
# If a label is not found in one Series or the other, the result will be None
print(b2[1:] + b2[:-1])
b3 = pd.Series(np.random.randn(3), name="something1")
print(b3)
print(b3.name)
b4 = b3.rename("something2")
print(b4)