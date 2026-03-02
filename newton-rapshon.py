import numpy as np

# fungsi
def fungsi(x):
    return x**3 - 2*x - 5

# turunan fungsi
def turunan(x):
    return 3*x**2 - 2

def newton_raphson(x0, eps, max_iter):
    i = 0
    x = x0
    
    while i < max_iter:
        fx = fungsi(x)
        fpx = turunan(x)
        
        if fpx == 0:
            print("Turunan nol, metode gagal.")
            return None
        
        x_baru = x - fx / fpx
        
        print(f"Iterasi {i}: x = {x:.6f}, f(x) = {fx:.6f}")
        
        if abs(x_baru - x) < eps:
            return x_baru
        
        x = x_baru
        i += 1
    
    return x

# contoh pemanggilan
akar = newton_raphson(4, 0.0001, 10)
print("Akar =", akar)