import numpy as np

def fungsi(x):
    return x - np.cos(x)

def bisection(a, b, eps):
    u = fungsi(a)
    v = fungsi(b)
    i = 0

    while ((b - a) / 2 > eps) and (i < 10):
        c = (a + b) / 2
        w = fungsi(c)

        if u * w < 0:
            b = c
            v = w
        else:
            a = c
            u = w

        i += 1

    return (a + b) / 2


print(bisection(0.5, 0.9, 0.01))