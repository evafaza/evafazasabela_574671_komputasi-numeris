import numpy as np

# Matriks koefisien (A)
A = np.array([
    [10, -1, 2],
    [-1, 11, -1],
    [2, -1, 10]
], dtype=float)

# Vektor hasil (b)
b = np.array([6, 25, -11], dtype=float)

# Jumlah variabel
n = len(b)

# Inisialisasi tebakan awal (x0)
x = np.zeros(n)

# Parameter iterasi
max_iter = 25
toleransi = 0.0001

print("Iterasi Jacobi:\n")

for k in range(max_iter):
    x_baru = np.zeros(n)

    for i in range(n):
        jumlah = 0
        for j in range(n):
            if j != i:
                jumlah += A[i][j] * x[j]

        # Rumus Jacobi :
        x_baru[i] = (b[i] - jumlah) / A[i][i]

    # Hitung error
    error = np.linalg.norm(x_baru - x, ord=np.inf)

    print(f"Iterasi ke-{k+1}: {x_baru}, error = {error}")

    # Cek konvergensi
    if error < toleransi:
        print("\nKonvergen!")
        break

    x = x_baru.copy()

print("\nHasil akhir:")
print(x_baru)