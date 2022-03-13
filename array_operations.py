import numpy as np

a1 = np.arange(10)
print(a1)
a1.shape = (2, 5)
print(a1)
a2 = np.arange(20)
a3 = a2[1:10:2]
print(a3)
a4 = np.array([[[1, 0],[2, 0],[3, 0]], [[4, 1],[5, 1],[6, 1]]])
print(a4.shape)
print(a4[1:])
a1[1] = 1 # Broadcastable
a1[1] = [1] # Broadcastable
# a1[1] = [1, 1] # Not broadcastable
print(a1)
print(a1[:, 2])
print(a1[:, 2:4])
# np.newaxis is an alias for None
print(a4[:, :, np.newaxis].shape) # Adds a new dimension to the resulting selection
print(a4[:, :, 0])

b1 = np.arange(10, 1, -1)
b2 = np.array([3, 3, 1, 8])
print(b1)
print(b2)
print(b1[b2])
b3 = np.arange(35).reshape(5, 7)
print(b3)
# 0 is broadcasted automatically for all 3 rows
print(b3[np.array([0, 2, 4]), 0]) # scalar value is used for all corresponding values
print(b3[np.array([0, 2, 4]), np.array([0, 1, 2])])
b4 = np.array([[1, 2], [3, 4], [5, 6]])
print(b4[1, [0, 1, 0]])
print(b4[:, [0, 1, 0]])