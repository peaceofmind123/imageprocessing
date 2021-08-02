import numpy as np
import matplotlib.pyplot as plt
import math
def zoomIn(M, n):
    h, k = M.shape
    accum = np.zeros((n * h, n * k))
    counter = 0
    # row replication
    for i in range(h):
        counter = 0

        for j in range(k):

            for l in range(counter, counter + n):
                accum[i, j + l] = M[i, j]

            counter += n-1

    # column replication
    temp = np.copy(accum)

    for j in range(n * k):
        counter = 0
        for i in range(h):

            for l in range(counter, counter + n):
                accum[i + l, j] = temp[i, j]

            counter += n-1

    return accum
s = plt.imread('../imgs/rose.tif')
b = zoomIn(s,4)
plt.imshow(b, cmap='gray')