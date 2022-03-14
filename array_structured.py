import numpy as np

a1 = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],
           dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
print(a1)
print(a1['age'])
a1['age'] = 5
print(a1)
a2 = np.dtype([('x', 'f4'), ('', 'i4'), ('z', 'i8')])
print(a2)
a3 = np.zeros(2, dtype='i8, f4, ?, S1')
print(a3)
a3[:] = 3
print(a3)
a3[:] = np.arange(2) # Cannot do a3 = np.arange(2) since it would entirely replace a3 with [0, 1]
print(a3)