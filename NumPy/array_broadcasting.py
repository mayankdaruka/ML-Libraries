import numpy as np

# a.shape = (5, 1)
# b.shape = (1, 6)
# c.shape = (6,)
# d.shape = ()
# All shapes are broadcastable to the dimension (5, 6)

a1 = np.array([1, 2, 3])
a2 = np.array([2, 2, 2])
print(a1 * a2)
# Scalar is stretched during the arithmetic operation to be shape shape as a1
print(a1 * 2) # More efficient - broadcasting moves less memory around during multiplication

b1 = np.array([0.0, 10.0, 20.0, 30.0])
b2 = np.array([1.0, 2.0, 3.0])
print(b1[:, np.newaxis] + b2) # Broadcasting happens here where 4x1 is stretched to 4x3
