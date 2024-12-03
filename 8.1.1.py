import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Өзгөрмөлөр жана параметрлер
x = sp.Symbol('x', positive=True)
c = sp.Symbol('c', positive=True)
ua, ub = 3, 0  # Чектик шарттар
a, b = 1, 2  # Интервал
k_x_c = c * x**3
f_x = 10 * x**(1/4)

# Дифференциалдык теңдеме
u = sp.Function('u')(x)
eq = sp.Eq(sp.diff(k_x_c * sp.diff(u, x), x), f_x)

# Жалпы чечим
general_sol = sp.dsolve(eq, u)

# Константаларды чектик шарттардан табуу
u_general = general_sol.rhs
boundary_eqs = [
    sp.Eq(u_general.subs(x, a), ua),
    sp.Eq(u_general.subs(x, b), ub)
]
constants = sp.solve(boundary_eqs, dict=True)[0]

# Акыркы чечим
u_solution = u_general.subs(constants)

# Графиктер үчүн параметрлер жана эсептөөлөр
param_values = [1, 2, 3, 4]  # c параметрлеринин топтому
x_vals = np.linspace(a, b, 300)

# Чечимдерди сандык түрдө баалоо
solutions = {
    f'c={value}': sp.lambdify(x, u_solution.subs(c, value), modules='numpy')(x_vals)
    for value in param_values
}

# Графикти тургузуу
plt.figure(figsize=(10, 6))
for label, y_vals in solutions.items():
    plt.plot(x_vals, y_vals, label=label)

plt.title("u(x) функциясынын c параметри үчүн графиги")
plt.xlabel("x")
plt.ylabel("u(x)")
plt.legend()
plt.grid()
plt.show()

# Акыркы чечимди көрсөтүү
print("u(x) аналитикалык чечими:")
sp.pprint(u_solution)
