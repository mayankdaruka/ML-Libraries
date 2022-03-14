# 6 ways to create NumPy arrays
# 1. Conversion from other python structures
# 2. NumPy array creation functions
# 3. Replicating, joining or mutating existing arrays
# 4. Reading arrays from disk
# 5. Creating arrays from raw bytes using strings/buffers
# 6. Use of special library functions (random etc.)

import numpy as np
from numpy.random import default_rng

# Default behavior is to create arrays in int64 and float
a1 = np.array([1, 2, 3, 4])
a2 = np.array([127, 128, 129], dtype=np.int8)
print(a2) # OVERFLOW

a3 = np.array([2, 3, 4], dtype=np.uint32)
a4 = np.array([5, 6, 7], dtype=np.uint32)
a5 = a3 - a4
print(a5) # Messed up output
print(a5.dtype) # uint32
a6 = a3 - a4.astype(np.int32)
print(a6)
print(a6.dtype) # int64 - can represent both differing types


b1 = np.arange(10)
print(b1)
b2 = np.arange(10, 23, dtype=np.float32)
print(b2)
b3 = np.arange(3, 5, 0.1)
print(b3.dtype)
b4 = np.linspace(1, 4, 6) # Creates arrays w/ specified # of elements spaced equally
print(b4)

c1 = np.eye(3) # Defines identity matrix
print(c1)
c2 = np.eye(4, 7, dtype=np.int8)
print(c2)
c3 = np.diag([1, 2, 3, 4])
print(c3)
c4 = np.diag([1, 2], 2)
print(c4)
c5 = np.diag(np.array([[1, 2], [3, 4]])) # Given 2D array it will return diagional elements
print(c5)
c6 = np.vander([1, 2, 3, 4], 3)
print(c6)

d1 = np.zeros((2, 3))
print(d1)
d2 = np.ones((2, 3, 1), dtype=np.int8)
print(d2)
print(default_rng(42).random((2, 3, 2)))

e1 = np.array([1, 2, 3, 4, 5, 6, 7])
e2 = e1[:2]
e2 += 1 # Mutates e1 also
e3 = e1[:2].copy() # If copy() was removed, both e1 and e2 would be mutated
e3 += 1
print(e1)
print(e2)
print(e3)