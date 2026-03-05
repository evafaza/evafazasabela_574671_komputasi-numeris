import numpy as np

# Matriks A dan vektor B
A = np.array([
    [2, -2, 2],
    [4, 2, -1],
    [2, -2, 4]
], dtype=float)
B = np.array([0, 7, 2], dtype=float)
# Membuat augmented matrix [A|B]
aug = np.column_stack((A, B))
print("Augmented Matrix Awal:")
print(aug)
print()
n = len(B)

# Gauss-Jordan elimination
for i in range(n):
    
    #Membuat privot menjadi 1
    privot = aug[i][i]
    aug[i] = aug[i] / privot 
    
    print(f"step {i+1}: Membagi baris {i+1} dengan privot {privot}")
    print(aug)
    print()
    
    # Eliminasi elemen kolom selain pivot
    for j in range(n):
        if j != i:
            factor = aug[j][i]
            aug[j] = aug[j] - factor * aug[i]

            
            print(f"Eliminasi baris {j+1} menggunakan baris {i+1}")
            print(aug)
            print()
            
# Solusi
solution = aug[:, -1]

print("=================================")
print("Solusi Sistem Persamaan")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])