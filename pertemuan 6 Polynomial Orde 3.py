import numpy as np
import matplotlib.pyplot as plt

# =========================
# DATA (Example 4)
# =========================
x = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52])
y = np.array([0.23, -0.23, -1.1, -0.45, 0.27, 0.1, -0.29, 0.24])

# =========================
# POLYNOMIAL ORDE 3
# =========================
coeff = np.polyfit(x, y, 3)  # derajat 3

# hasil koefisien
d, c, b, a = coeff  # urutan dari pangkat tertinggi

print("=== HASIL POLYNOMIAL ORDE 3 ===")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

# =========================
# FUNGSI POLINOM
# =========================
def f(x):
    return a + b*x + c*x**2 + d*x**3

# =========================
# PLOT (kayak GeoGebra)
# =========================
x_smooth = np.linspace(min(x), max(x), 200)
y_smooth = f(x_smooth)

plt.figure()

# titik data
plt.scatter(x, y, s=60, label="Data Asli")

# kurva polynomial
plt.plot(x_smooth, y_smooth, linewidth=2, label="Polynomial Orde 3")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Regression Orde 3")
plt.legend()
plt.grid()

plt.show()