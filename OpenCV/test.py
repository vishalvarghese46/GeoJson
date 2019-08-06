import numpy as np

a = np.array([[(1,2,3,4),
              (6,7,8,9),
              (6,7,8,9)]])
print(a.size)
print(a.shape)
print(a.ndim)
#print(a[0][3], a[1][1], a[2][3])
#print(f'Printing third element from each row: {a[0:,1]}')


b = np.arange(1000)
print(b.size)
print(b.shape)
print(b.ndim)