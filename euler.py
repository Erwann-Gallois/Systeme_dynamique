import numpy as np
import matplotlib.pyplot as plt

def flg(y, t):
    r = 3
    K = 1
    return r*y*(1-(y/K))
# t -> liste des temps donné
def euler (y0, f, t):
    N = len(t)
    y = [0] * N
    y[0] = y0
    print(y)
    for i in range(1, N):
        y[i] = y[i-1] + (t[i]-t[i-1])*f(y[i-1], t[i-1])
    return y

print(euler(0.1, flg, [0,1,2,3,4,5,6,7,8,9,10]))