# GAUSS-SEIDEL METHOD - EXAMPLE 1 (PITFALL)

# Initial guess
a1 = 1.0
a2 = 2.0
a3 = 5.0

# Parameter
tolerance = 0.0001
max_iter = 10  # dibatasi karena biasanya tidak konvergen

print("Iterasi |    a1        a2        a3        Error (%)")
print("-"*55)

for i in range(max_iter):
    a1_old = a1
    a2_old = a2
    a3_old = a3

    # Update sesuai persamaan PDF
    a1 = (106.8 - 5*a2 - a3) / 25
    a2 = (177.2 - 6*a1 - a3) / 4
    a3 = (279.2 - a1 - 2*a2) / 144

    # Hitung error (%)
    e1 = abs((a1 - a1_old) / a1) * 100 if a1 != 0 else 0
    e2 = abs((a2 - a2_old) / a2) * 100 if a2 != 0 else 0
    e3 = abs((a3 - a3_old) / a3) * 100 if a3 != 0 else 0

    error_max = max(e1, e2, e3)

    print(f"{i+1:7d} | {a1:9.5f} {a2:9.5f} {a3:9.5f} {error_max:12.6f}")

# Output akhir
print("\n=== HASIL AKHIR (tidak konvergen) ===")
print(f"a1 = {a1:.5f}")
print(f"a2 = {a2:.5f}")
print(f"a3 = {a3:.5f}")