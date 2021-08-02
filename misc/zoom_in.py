import numpy as np
import math


def zoom_in(M:np.ndarray, n):
    (h,k) = M.shape
    accum = np.zeros((n*h, n*k))

    # row replication
    for i in range(h):
        counter = 0
        for j in range(k):
            for l in range(counter, counter + n):
                accum[i,j+l] = M[i][j]
                counter += 1


    # column replication
    temp = np.copy(accum)

    for j in range(n*k):
        counter = 0
        for i in range(h):
            for l in range(counter, counter + n):
                accum[i + l, j] = temp[i][j]
                counter += 1

    return accum

M = np.array([[1,2,3],[4,5,6]])
n = 2
print(zoom_in(M,n))