import numpy as np

# fungsi
def fungsi(x):
    return x**3 - 2*x - 5

# turunan fungsi
def turunan(x):
    return 3*x**2 - 2

def newton_raphson(x0, eps, max_iter):
    print("-------------------------------------------------------------")
    print(" k        xk         f(xk)        f'(xk)        ERROR")
    print("-------------------------------------------------------------")
    
    x = x0
    
    for k in range(max_iter):
        fx = fungsi(x)
        fpx = turunan(x)
        
        if fpx == 0:
            print("Turunan nol, metode gagal.")
            return None
        
        x_baru = x - fx / fpx
        error = abs(x_baru - x)
        
        print(f"{k:<2}  {x:>10.6f}  {fx:>12.6f}  {fpx:>12.6f}  {error:>10.6f}")
        
        if error < eps:
            print("-------------------------------------------------------------")
            return x_baru
        
        x = x_baru
    
    print("-------------------------------------------------------------")
    return x

# contoh pemanggilan
akar = newton_raphson(4, 0.0001, 10)
print("\nAkar =", akar)