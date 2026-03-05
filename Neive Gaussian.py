import numpy as np

# Matriks koefisien
A = np.array([
    [6, -2, 2, 4],
    [12, -8, 6, 10],
    [3, -13, 9, 3],
    [-6, 4, 1, -18]
], dtype=float)

# Matriks hasil
B = np.array([16, 26, -19, -34], dtype=float)

n = len(B)

# Gabungkan A dan B menjadi augmented matrix
aug = np.column_stack((A, B))

print("Augmented Matrix Awal")
print(aug)

# =========================
# Forward Elimination
# =========================
for i in range(n-1):
    for j in range(i+1, n):
        factor = aug[j][i] / aug[i][i]
        aug[j, i:] = aug[j, i:] - factor * aug[i, i:]

print("\nSetelah forward Elimination:")
print(aug)

# =========================
# Backward Substitution
# =========================
x = np.zeros(n)

for i in range(n-1, -1, -1):
    x[i] = aug[i][n]
    
    for j in range(i+1, n):
        x[i] -= aug[i][i]
    
    x[i] = x[i] / aug[i][i]

print("\nsolusi:")
for i in range(n):
    print(f"x{i+1} =", x[i])