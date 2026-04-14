# ===============================
# 1. Linear Interpolation (sin 0.15)
# ===============================
print("=== Linear Interpolation sin(0.15) ===")

x0, y0 = 0.1, 0.0998
x1, y1 = 0.2, 0.1987
x = 0.15

m = (y1 - y0) / (x1 - x0)
f_x = y0 + m * (x - x0)

print("Slope (m) =", m)
print("f(0.15) =", f_x)


# ===============================
# 2. Linear Interpolation (Viscosity)
# ===============================
print("\n=== Linear Interpolation Viscosity ===")

T0, V0 = 5, 1.519
T1, V1 = 10, 1.308
T = 8

m = (V1 - V0) / (T1 - T0)
V = V0 + m * (T - T0)

print("Slope (m) =", m)
print("V(8) =", V)


# ===============================
# 3. Divided Difference (Manual Data)
# ===============================
print("\n=== Divided Difference (Data 1) ===")

x = [0, 1, -1]
y = [-5, -3, -15]

n = len(x)
dd = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dd[i][0] = y[i]

for j in range(1, n):
    for i in range(n - j):
        dd[i][j] = (dd[i+1][j-1] - dd[i][j-1]) / (x[i+j] - x[i])

for row in dd:
    print(row)


# ===============================
# 4. Polynomial Newton
# ===============================
print("\n=== Polynomial Newton ===")

f0 = -5
f01 = 2
f012 = -4

def f(x):
    return f0 + f01*(x - 0) + f012*(x - 0)*(x - 1)

print("f(x) = -5 + 2(x) -4(x)(x-1)")
print("f(2) =", f(2))


# ===============================
# 5. Lagrange Interpolation (Case 1)
# ===============================
print("\n=== Lagrange (Case 1) ===")

X = [1/3, 1/4, 1]
Y = [2, -1, 7]

def lagrange(x, X, Y):
    result = 0
    n = len(X)

    for i in range(n):
        term = Y[i]
        for j in range(n):
            if i != j:
                term *= (x - X[j]) / (X[i] - X[j])
        result += term

    return result

print("P(0.5) =", lagrange(0.5, X, Y))


# ===============================
# 6. Lagrange Interpolation (Case 2)
# ===============================
print("\n=== Lagrange (Case 2) ===")

X = [0,1,2,3,4]
Y = [1,3,2,5,4]

print("P(2.5) =", lagrange(2.5, X, Y))


# ===============================
# 7. Divided Difference (General Function)
# ===============================
print("\n=== Divided Difference (General) ===")

x = [2,4,5,6,7]
y = [3,5,1,6,9]

def divided_diff(x, y):
    n = len(x)
    table = [[0]*n for _ in range(n)]

    for i in range(n):
        table[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])

    return table

table = divided_diff(x, y)

for row in table:
    print(row)


# ===============================
# 8. Lagrange (Inverse Interpolation)
# ===============================
print("\n=== Lagrange Inverse ===")

X = [3.2, 2.0, 1.6]
Y = [1, 2, 3]

print("Hasil inverse =", lagrange(2.5, X, Y))