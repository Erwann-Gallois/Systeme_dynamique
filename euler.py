import numpy as np
import matplotlib.pyplot as plt

def flg(N,t):
    r = 3
    K = 1
    return r*N*(1-(N/K))

def Euler(h, n, t0, y0, f):

    t = [0] * (int(n/h)+1)
    t[0] = t0

    y = [0] * len(t)
    y[0] = y0

    for i in range(1,len(t)):
        t[i] = t[i-1] + h
        y[i] = y[i-1] + (t[i]-t[i-1]) * f(y[i-1], t[i-1]) 
    return y

print(Euler(0.1, 10, 0, 0.1, flg))