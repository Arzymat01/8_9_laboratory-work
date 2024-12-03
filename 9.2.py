# Import required libraries
from mpl_toolkits.mplot3d import Axes3D  # 3D графиктерди түзүү үчүн
import numpy as np  # Массивдерди жана математикалык операцияларды колдонуу үчүн
import matplotlib.pyplot as plt  # Графиктерди түзүү үчүн

# Parameters for the grid
L = 1  # Мейкиндик диапазону: 0 <= x <= L
T = 0.1  # Убакыт диапазону: 0 <= t <= T
Nx = 50  # Мейкиндик боюнча чекиттердин саны
Nt = 100  # Убакыт боюнча чекиттердин саны
dx = L / Nx  # Мейкиндиктеги чекиттер ортосундагы аралык
dt = T / Nt  # Убакыттагы чекиттер ортосундагы аралык

# Spatial and temporal grid points
x = np.linspace(0, L, Nx + 1)  # Мейкиндик чекиттери үчүн массив
t = np.linspace(0, T, Nt + 1)  # Убакыт чекиттери үчүн массив

# Initial condition
def phi(x):  # Баштапкы шарт: u(x, 0) = phi(x)
    return np.sin(np.pi * x)  # Баштапкы шарт катары синус толкунун колдонуу

# f(x, t) function (forcing term)
def f(x, t):  # Теңдеменин оң тарабындагы функция
    return 0  # Бул мисалда сырткы күч колдонулбайт (f = 0)

# Boundary conditions
def alpha(t):  # x=0 чектик шарт: ∂u/∂x |x=0 = alpha(t)
    return 0  # Бул жерде чектик шарт нөлгө барабар

def beta(t):  # x=1 чектик шарт: u(1, t) = beta(t)
    return 0  # Бул жерде чектик шарт нөлгө барабар

# Initialize the solution array
u = np.zeros((Nx + 1, Nt + 1))  # u(x, t) үчүн нөлдөр массивин түзүү
u[:, 0] = phi(x)  # Баштапкы шартты колдонуу: u(x, 0) = phi(x)

# Solve using finite difference method
for n in range(0, Nt):  # Убакыт боюнча итерация (бардык убакыт катмарлары)
    for i in range(1, Nx):  # Мейкиндик боюнча итерация (чектик чекиттерди кошпогондо)
        x_term = (x[i] + 3) / (dx ** 2)  # Мейкиндик боюнча коэффициент
        u[i, n + 1] = (  # u(x_i, t_{n+1}) жаңы убакыт катмарындагы маанини эсептөө
            u[i, n]  # Мурдагы убакыт катмарынын мааниси
            + dt * (  # Убакыт коэффициенти менен маанилердин өзгөрүшү
                x_term * (u[i + 1, n] - 2 * u[i, n] + u[i - 1, n])  # Мейкиндик боюнча экинчи туунду
                - x[i] * u[i, n]  # Потенциалдык мүчө
                + f(x[i], t[n])  # Кошумча функциянын учурдагы мааниси
            )
        )

    # Apply boundary conditions
    u[0, n + 1] = u[1, n + 1] - dx * alpha(t[n + 1])  # x=0 үчүн чектик шартты колдонуу
    u[Nx, n + 1] = beta(t[n + 1])  # x=1 үчүн чектик шартты колдонуу

# Create a meshgrid for plotting
X, T = np.meshgrid(x, t, indexing='ij')  # Мейкиндик жана убакыт боюнча сетканы түзүү

# 3D визуалдаштыруу
fig = plt.figure(figsize=(12, 8))  # Графиктин көлөмүн аныктоо
ax = fig.add_subplot(111, projection='3d')  # 3D огу менен субплот түзүү

# 3D беттик графикти түзүү
surf = ax.plot_surface(T, X, u, cmap='viridis', edgecolor='none')  # Беттин сүрөтүн тартуу

# Окторду жана аталышты белгилөө
ax.set_xlabel('Time (t)')  # Убакыт огу
ax.set_ylabel('Space (x)')  # Мейкиндик огу
ax.set_zlabel('u(x, t)')  # Чечимдин мааниси
ax.set_title('Solution of the Parabolic Equation in 3D')  # Графиктин аталышы

# Түс шкаласын кошуу
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='u(x, t)')  # Түс шкаласын көрсөтүү

plt.show()  # Графикти көрсөтүү
