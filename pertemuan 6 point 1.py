import numpy as np

# =========================
# DATA (Example 4)
# =========================
x = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52])
y = np.array([0.23, -0.23, -1.1, -0.45, 0.27, 0.1, -0.29, 0.24])

# =========================
# HITUNG SEMUA KOLOM (TABEL)
# =========================
lnx = np.log(x)
cosx = np.cos(x)
ex = np.exp(x)

lnx2 = lnx**2
lnx_cosx = lnx * cosx
lnx_ex = lnx * ex
y_lnx = y * lnx

cosx2 = cosx**2
cosx_ex = cosx * ex
y_cosx = y * cosx

ex2 = ex**2
y_ex = y * ex

# =========================
# TAMPILKAN TABEL
# =========================
print("=== TABEL PERHITUNGAN ===")
print("i | x | y | ln(x)^2 | ln(x)cos(x) | ln(x)e^x | yln(x)")
for i in range(len(x)):
    print(f"{i+1} | {x[i]:.2f} | {y[i]:.2f} | {lnx2[i]:.4f} | {lnx_cosx[i]:.4f} | {lnx_ex[i]:.4f} | {y_lnx[i]:.4f}")

# =========================
# HITUNG SIGMA
# =========================
S_lnx2 = np.sum(lnx2)
S_lnx_cosx = np.sum(lnx_cosx)
S_lnx_ex = np.sum(lnx_ex)

S_cosx2 = np.sum(cosx2)
S_cosx_ex = np.sum(cosx_ex)

S_ex2 = np.sum(ex2)

S_y_lnx = np.sum(y_lnx)
S_y_cosx = np.sum(y_cosx)
S_y_ex = np.sum(y_ex)

# =========================
# TAMPILKAN SIGMA
# =========================
print("\n=== HASIL SIGMA ===")
print("Σ ln(x)^2 =", S_lnx2)
print("Σ ln(x)cos(x) =", S_lnx_cosx)
print("Σ ln(x)e^x =", S_lnx_ex)
print("Σ cos(x)^2 =", S_cosx2)
print("Σ cos(x)e^x =", S_cosx_ex)
print("Σ e^x^2 =", S_ex2)
print("Σ y ln(x) =", S_y_lnx)
print("Σ y cos(x) =", S_y_cosx)
print("Σ y e^x =", S_y_ex)

# =========================
# NORMAL EQUATION
# =========================
A = np.array([
    [S_lnx2,     S_lnx_cosx, S_lnx_ex],
    [S_lnx_cosx, S_cosx2,    S_cosx_ex],
    [S_lnx_ex,   S_cosx_ex,  S_ex2]
])

B = np.array([S_y_lnx, S_y_cosx, S_y_ex])

# =========================
# SOLUSI
# =========================
a, b, c = np.linalg.solve(A, B)

print("\n=== HASIL AKHIR ===")
print("a =", a)
print("b =", b)
print("c =", c)