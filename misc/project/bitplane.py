import numpy as np
import matplotlib.pyplot as plt
import math
genius = plt.imread('../imgs/einstein.tif')
def sliceOnBit(M, b):
    h, k = M.shape
    accum = np.zeros((h, k))
    # 8 bit masks
    ms = [1,2,4,8,16,32,64,128 ]
    for i in range(h):
        for j in range(k):
            accum[i, j] = 255 if M[i, j] & ms[b - 1] > 0 else 0

    return accum

msb = sliceOnBit(genius, 7)