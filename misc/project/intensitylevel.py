import numpy as np
import matplotlib.pyplot as plt
import math
# intensity level resolution

# L levels to L/n levels
# i.e. (0,n-1) -> 0
#      (n,2n-1)-> 1
#   ...(L-n,L-1) -> L/n-1

def reduceResolution(M, n):
    h, k = M.shape
    accum = np.zeros((h, k))
    d = dict()
    # reverse index construction
    for r in range(0, math.ceil(256 / n)):
        for v in range(256):
            if r * n <= v and v <= (r + 1) * n - 1:
                d[str(v)] = r

    for i in range(h):
        for j in range(k):
            accum[i, j] = d[str(int(M[i, j]))]

    return accum


lena = plt.imread('../imgs/lena.tif')
reduced = reduceResolution(lena, 2)
