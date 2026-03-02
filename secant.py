import numpy as np

# fungsi
def fungsi(x):
    return x - np.cos(x)

def secant(x0, x1, eps, max_iter):
    print("-------------------------------------------------------------")
    print(" k        xk            f(xk)         ERROR")
    print("-------------------------------------------------------------")
    
    for k in range(max_iter):
        f0 = fungsi(x0)
        f1 = fungsi(x1)
        
        if (f1 - f0) == 0:
            print("Pembagian nol, metode gagal.")
            return None
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        error = abs(x2 - x1)
        
        print(f"{k:<2}  {x1:>12.8f}  {f1:>12.8f}  {error:>12.8f}")
        
        if error < eps:
            print("-------------------------------------------------------------")
            return x2
        
        x0 = x1
        x1 = x2
    
    print("-------------------------------------------------------------")
    return x1

# contoh pemanggilan
akar = secant(0.6, 0.8, 1e-10, 10)
print("\nAkar =", akar)