import numpy as np

a = np.array([[1,2,3,4],
              (6,7,8,9),
              [1,2,3,4]])
print(a.size)
print(a.shape)
print(a.ndim)
#print(a[0][1], a[1][1], a[2][3])
print(f'Printing third element from each row: {a[0:,3]}')
'''
print("\n")
b = np.arange(1000)
print(b.size)
print(b.shape)
print(b.ndim)

myArray = np.array([(1,2,3,4), (3,4,5,6), (7,8,9,10)])

print(myArray.max(axis=0))

print(myArray.sum(axis=1))

print(f'The standard deviation is: {np.std(myArray)}')


a = np.array([[1,2,3,4],
             [1,2,3,4],
            [1,2,3,4],
             [1,2,3,4]])

b = np.array([[1,2,3,4],
             [1,2,3,4],
            [1,2,3,4],
             [1,2,3,4]])

print(a.dot(b).shape)
print(np.matmul(a,b))
print(b.ndim)
print(b.shape)
'''