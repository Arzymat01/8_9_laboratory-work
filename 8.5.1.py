import numpy as np
import matplotlib.pyplot as plt

# Белгиленген туруктуулар
pi = np.pi
T = 0.1  # убакыттын акыркы чекити

# u(x, t) функциясы
def u(x, t):
    return np.exp(-pi**2 * t) * np.sin(pi * x)

# x жана t маанилерин даярдоо
x = np.linspace(0, 1, 100)  # [0, 1] аралыгында x чекиттери
t_values = [0, 0.02, 0.05, 0.1]  # t убакыт чекиттери

# u(x, t) функциясын графикке чыгаруу
plt.figure(figsize=(8, 6))
for t in t_values:
    plt.plot(x, u(x, t), label=f"t = {t:.2f}")

# Графиктин кооздолушу
plt.title("u(x, t) = exp(-π²t) * sin(πx)")
plt.xlabel("x")
plt.ylabel("u(x, t)")
plt.legend()
plt.grid(True)
plt.show()
