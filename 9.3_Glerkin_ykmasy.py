import numpy as np
import matplotlib.pyplot as plt

# Белгиленген параметрлер
pi = np.pi
T = 0.1  # Убакыттын акыркы чекити
N = 1    # Негизги функциялардын саны

# Баштапкы функция
def phi(x):
    return np.sin(pi * x)

# Коэффициенттердин баштапкы шарттары
def c_n(n):
    return 2 * np.trapz(phi(x) * np.sin(n * pi * x), x)

# Галеркин ыкмасы боюнча чечим
def u_galerkin(x, t, N):
    u = np.zeros_like(x)
    for n in range(1, N+1):
        c_n0 = c_n(n)
        u += c_n0 * np.exp(-(n * pi)**2 * t) * np.sin(n * pi * x)
    return u

# x жана t маанилерин даярдоо
x = np.linspace(0, 1, 100)  # [0, 1] аралыгында x чекиттери
t_values = [0, 0.02, 0.05, 0.1]  # t убакыт чекиттери

# Галеркин ыкмасынын графиги
plt.figure(figsize=(8, 6))
for t in t_values:
    plt.plot(x, u_galerkin(x, t, N), label=f"t = {t:.2f}")

# Графиктин кооздолушу
plt.title("Галеркин ыкмасы менен эсептелген u(x, t)")
plt.xlabel("x")
plt.ylabel("u(x, t)")
plt.legend()
plt.grid(True)
plt.show()
