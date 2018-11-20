import numpy as np
N = 4
M = np.arange(start = 1, stop = 33)
X = np.array([M.T],  ndmin=2)
m = np.asmatrix(np.tile(X,(N,1)))

def closest(z, A):
    array = np.asarray(A)
    idx = np.abs(array - z).argmin()
    return array[idx]

array = np.arange(1,50,2.4)
print(array)

print(closest(5,array))