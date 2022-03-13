import numpy as np

a1 = np.array([1, 2, 3], dtype='f')
print(a1, a1.dtype)
print(a1.astype(np.uint16))
print(a1.astype(np.bool8))
print(np.int16(a1))
print(np.issubdtype(a1.dtype, np.integer))
print(np.issubdtype(a1.dtype, np.floating))

print(np.power(100, 7, dtype=np.int64))
print(np.power(100, 7, dtype=np.int32)) # Overflow

print(np.iinfo(int))
print(np.iinfo(np.int32))
print(np.iinfo(np.uint32))
print(np.finfo(np.float32))
print(np.finfo(np.longdouble))