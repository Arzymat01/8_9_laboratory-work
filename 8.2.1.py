import numpy as np
import matplotlib.pyplot as plt


def p(x):
    return 0.5 + np.sin(x) ** 2


def q(x):
    return 2 * (1 + x ** 2)


def f(x):
    return 10 * (1 + np.sin(x) ** 2)


def solve_diff_eq(a, b, ua, ub, h):
    # Number of internal points
    n = int((b - a) / h) - 1
    x = np.linspace(a + h, b - h, n)

    # Create coefficient matrix A
    A = np.zeros((n, n))
    B = np.zeros(n)

    # Fill matrix A and vector B
    for i in range(n):
        # Diagonal elements
        A[i, i] = -2 / h ** 2 - q(x[i])

        # Off-diagonal elements
        if i > 0:
            A[i, i - 1] = 1 / h ** 2 + p(x[i]) / (2 * h)
        if i < n - 1:
            A[i, i + 1] = 1 / h ** 2 - p(x[i]) / (2 * h)

        # Right-hand side
        B[i] = -f(x[i])

        # Boundary conditions
        if i == 0:
            B[i] -= (1 / h ** 2 + p(x[i]) / (2 * h)) * ua
        if i == n - 1:
            B[i] -= (1 / h ** 2 - p(x[i]) / (2 * h)) * ub

    # Solve system
    u = np.linalg.solve(A, B)

    # Include boundary points
    x_full = np.concatenate(([a], x, [b]))
    u_full = np.concatenate(([ua], u, [ub]))

    return x_full, u_full


# Parameters
a, b = 0, 2
ua, ub = 0, 4
epsilon = 0.02

# Solve with initial step size
h1 = 0.2
x1, u1 = solve_diff_eq(a, b, ua, ub, h1)

# Solve with halved step size
h2 = h1 / 2
x2, u2 = solve_diff_eq(a, b, ua, ub, h2)

# Calculate maximum difference
diff = np.max(np.abs(np.interp(x1, x2, u2) - u1))
print(f"Difference between solutions: {diff}")

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(x1, u1, 'o-', label=f'h = {h1}')
plt.plot(x2, u2, 's-', label=f'h = {h2}')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Numerical Solution of Differential Equation')
plt.legend()
plt.grid(True)
plt.show()