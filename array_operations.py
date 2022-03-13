from cmath import isnan
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

c1 = np.array([[ 0,  1,  2], [ 3,  4,  5], [ 6,  7,  8], [ 9, 10, 11]])
c1_rows = np.array([[0, 1], [2, 3]], dtype=np.intp)
c1_columns = np.array([1, 1], dtype=np.intp)
print(c1[c1_rows])
print(c1[c1_rows, c1_columns])
c1_rows = np.array([0, 3], dtype=np.intp)
c1_columns = np.array([0, 2], dtype=np.intp)
print(c1[c1_rows])
print(c1[c1_rows[:, None]])
print(c1[c1_rows[:, None], c1_columns])

d1 = np.array([[1., 2.], [np.nan, 3.], [np.nan, np.nan]])
print(d1)
print(~np.isnan(d1))
print(d1[~np.isnan(d1)]) # Prints all the values corresponding to True in an array
d2 = np.array([1, -2, -3, 5])
print(d2 < 0)
print(d2[d2 < 0] - 20)
d3 = np.arange(35).reshape(5, 7)
d3 = d3 > 20
print(d3[:, 5])
d4 = np.array([[0, 1, 3], [1, 1, 5], [2, 2, 6]])
print(d4.sum(0)) # Vertical axis
print(d4.sum(1)) # Horizontal axis
print(d4[d4.sum(1) < 8])

e1 = np.arange(35).reshape(5,7)
e2 = e1[np.array([0, 2, 4]), 1:3]
print(e2)
print(e1[:, 1:3][np.array([0, 2, 4]), :]) # Same thing

f1 = np.zeros((2, 2), dtype=[('a', np.int32), ('b', np.float64, (3, 3))])
print(f1)
f2 = np.arange(10)
f2[2:7] = 1.2  # the 1.2 converted to 1
print(f2)
f3 = np.arange(81).reshape(3, 3, 3, 3)
print(f3[1, 1, 1, 1])