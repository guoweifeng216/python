import numpy as np

b = np.arange(9).reshape(3,3)
print b
print b.ravel()
c = np.arange(27).reshape(3,3,3)
print c
print c.ravel()
# print b[1]
# print b[1][1]