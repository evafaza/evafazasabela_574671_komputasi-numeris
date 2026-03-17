# GAUSS-SEIDEL METHOD 


# Matriks koefisien
A = [
    [12, 3, -5],
    [1, 5, 3],
    [3, 7, 13]
]

# Vektor konstanta
b = [1, 2, 3]

# Initial guess
x = [0.0, 0.0, 0.0]

# Parameter
tolerance = 0.0001
max_iter = 50

print("Iterasi |    x1        x2        x3        Error (%)")
print("-"*55)

# Iterasi Gauss-Seidel
for k in range(max_iter):
    x_old = x.copy()

    # Update nilai
    x[0] = (b[0] - A[0][1]*x[1] - A[0][2]*x[2]) / A[0][0]
    x[1] = (b[1] - A[1][0]*x[0] - A[1][2]*x[2]) / A[1][1]
    x[2] = (b[2] - A[2][0]*x[0] - A[2][1]*x[1]) / A[2][2]

    # Hitung error relatif (%)
    errors = []
    for i in range(3):
        if x[i] != 0:
            err = abs((x[i] - x_old[i]) / x[i]) * 100
        else:
            err = 0
        errors.append(err)

    error_max = max(errors)

    # Tampilkan hasil iterasi
    print(f"{k+1:7d} | {x[0]:9.5f} {x[1]:9.5f} {x[2]:9.5f} {error_max:12.6f}")

    # Cek konvergensi
    if error_max < tolerance:
        break

# Output akhir
print("\n=== HASIL AKHIR ===")
print(f"x1 = {x[0]:.5f}")
print(f"x2 = {x[1]:.5f}")
print(f"x3 = {x[2]:.5f}")