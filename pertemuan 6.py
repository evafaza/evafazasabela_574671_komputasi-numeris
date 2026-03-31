import numpy as np
import matplotlib.pyplot as plt

# =========================
# DATA DARI PPT
# =========================
x = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52])
y = np.array([0.23, -0.23, -1.1, -0.45, 0.27, 0.1, -0.29, 0.24])

# =========================
# HITUNG SEMUA KOMPONEN
# =========================
lnx = np.log(x)
cosx = np.cos(x)
ex = np.exp(x)

# sesuai tabel
lnx2 = lnx**2
cosx2 = cosx**2
ex2 = ex**2

lnx_cosx = lnx * cosx
lnx_ex = lnx * ex
cosx_ex = cosx * ex

y_lnx = y * lnx
y_cosx = y * cosx
y_ex = y * ex

# =========================
# HITUNG SEMUA SIGMA
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
# BENTUK MATRIX NORMAL EQUATION
# =========================
A = np.array([
    [S_lnx2,     S_lnx_cosx, S_lnx_ex],
    [S_lnx_cosx, S_cosx2,    S_cosx_ex],
    [S_lnx_ex,   S_cosx_ex,  S_ex2]
])

B = np.array([S_y_lnx, S_y_cosx, S_y_ex])

# =========================
# SOLUSI (a, b, c)
# =========================
coeff = np.linalg.solve(A, B)
a, b, c = coeff

print("Koefisien:")
print("a =", a)
print("b =", b)
print("c =", c)

# =========================
# FUNGSI HASIL FITTING
# =========================
def f(x):
    return a*np.log(x) + b*np.cos(x) + c*np.exp(x)

# =========================
# PLOT (SEPERTI GEOGEBRA)
# =========================
x_smooth = np.linspace(min(x), max(x), 200)
y_smooth = f(x_smooth)

plt.figure()
plt.scatter(x, y, label='Data Asli')  # titik
plt.plot(x_smooth, y_smooth, label='Kurva Fitting')  # kurva

plt.xlabel("x")
plt.ylabel("y")
plt.title("Nonlinear Least Squares Fit (Example 4)")
plt.legend()
plt.grid()

plt.show()