# ============================================================
# NUMERICAL DIFFERENTIATION & RICHARDSON EXTRAPOLATION
# Thesis Implementation
# Case Study:
# y = log(x)
# x = 25
# h = 5
#
# 1. Forward Difference O(h)
# 2. Backward Difference O(h)
# 3. True Percent Relative Error
# 4. Richardson Extrapolation
# ============================================================

import math

# ============================================================
# FUNCTION DEFINITIONS
# ============================================================

# Function y = log(x)
# menggunakan natural logarithm ln(x)
def f(x):
    return math.log(x)

# True derivative of ln(x)
# d/dx ln(x) = 1/x
def true_derivative(x):
    return 1 / x

# ============================================================
# FORWARD DIFFERENCE O(h)
# f'(x) ≈ [f(x+h) - f(x)] / h
# ============================================================

def forward_difference(x, h):
    return (f(x + h) - f(x)) / h

# ============================================================
# BACKWARD DIFFERENCE O(h)
# f'(x) ≈ [f(x) - f(x-h)] / h
# ============================================================

def backward_difference(x, h):
    return (f(x) - f(x - h)) / h

# ============================================================
# TRUE PERCENT RELATIVE ERROR
# Et = |(true - approx)/true| × 100%
# ============================================================

def true_percent_relative_error(true_value, approx_value):
    return abs((true_value - approx_value) / true_value) * 100

# ============================================================
# RICHARDSON EXTRAPOLATION
#
# Formula:
# D_rich = D(h/2) + [D(h/2) - D(h)] / (2^p - 1)
#
# p = order of truncation error
# untuk forward/backward difference O(h), maka p = 1
# ============================================================

def richardson_extrapolation(D_h, D_h2, p):
    return D_h2 + (D_h2 - D_h) / (2**p - 1)

# ============================================================
# MAIN PROGRAM
# ============================================================

# Given values
x = 25
h = 5

print("=" * 65)
print("NUMERICAL DIFFERENTIATION OF y = ln(x)")
print("=" * 65)

# ------------------------------------------------------------
# TRUE DERIVATIVE
# ------------------------------------------------------------

true_value = true_derivative(x)

print(f"\nTrue derivative at x = {x}")
print(f"f'(x) = 1/x = {true_value:.10f}")

# ============================================================
# PART 1
# FORWARD & BACKWARD DIFFERENCE
# ============================================================

print("\n" + "=" * 65)
print("PART 1 : FORWARD AND BACKWARD DIFFERENCE")
print("=" * 65)

# Forward difference
forward_approx = forward_difference(x, h)

# Backward difference
backward_approx = backward_difference(x, h)

# Errors
forward_error = true_percent_relative_error(true_value, forward_approx)
backward_error = true_percent_relative_error(true_value, backward_approx)

# Display results
print("\nFORWARD DIFFERENCE O(h)")
print(f"Approximation = {forward_approx:.10f}")
print(f"True Percent Relative Error = {forward_error:.6f}%")

print("\nBACKWARD DIFFERENCE O(h)")
print(f"Approximation = {backward_approx:.10f}")
print(f"True Percent Relative Error = {backward_error:.6f}%")

# ============================================================
# PART 2
# RICHARDSON EXTRAPOLATION
# ============================================================

print("\n" + "=" * 65)
print("PART 2 : RICHARDSON EXTRAPOLATION")
print("=" * 65)

# Use h and h/2
h2 = h / 2

# Forward difference with h
D_forward_h = forward_difference(x, h)

# Forward difference with h/2
D_forward_h2 = forward_difference(x, h2)

# Backward difference with h
D_backward_h = backward_difference(x, h)

# Backward difference with h/2
D_backward_h2 = backward_difference(x, h2)

# Richardson extrapolation
# p = 1 karena metode O(h)
forward_richardson = richardson_extrapolation(
    D_forward_h,
    D_forward_h2,
    p=1
)

backward_richardson = richardson_extrapolation(
    D_backward_h,
    D_backward_h2,
    p=1
)

# Errors after Richardson
forward_rich_error = true_percent_relative_error(
    true_value,
    forward_richardson
)

backward_rich_error = true_percent_relative_error(
    true_value,
    backward_richardson
)

# Display results
print("\nFORWARD DIFFERENCE + RICHARDSON")
print(f"D(h)     = {D_forward_h:.10f}")
print(f"D(h/2)   = {D_forward_h2:.10f}")
print(f"Richardson Result = {forward_richardson:.10f}")
print(f"True Percent Relative Error = {forward_rich_error:.6f}%")

print("\nBACKWARD DIFFERENCE + RICHARDSON")
print(f"D(h)     = {D_backward_h:.10f}")
print(f"D(h/2)   = {D_backward_h2:.10f}")
print(f"Richardson Result = {backward_richardson:.10f}")
print(f"True Percent Relative Error = {backward_rich_error:.6f}%")

# ============================================================
# FINAL COMPARISON
# ============================================================

print("\n" + "=" * 65)
print("FINAL COMPARISON")
print("=" * 65)

print(f"""
True Value                     = {true_value:.10f}

Forward Difference             = {forward_approx:.10f}
Forward Error                  = {forward_error:.6f}%

Backward Difference            = {backward_approx:.10f}
Backward Error                 = {backward_error:.6f}%

Forward Richardson             = {forward_richardson:.10f}
Forward Richardson Error       = {forward_rich_error:.6f}%

Backward Richardson            = {backward_richardson:.10f}
Backward Richardson Error      = {backward_rich_error:.6f}%
""")

print("=" * 65)
print("PROGRAM FINISHED")
print("=" * 65)