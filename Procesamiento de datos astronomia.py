import numpy as np
import matplotlib.pyplot as plt
import astropy as astropy  





# Generar datos de ejemplo
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 2 * x + 1 + np.random.randn(100)

# Graficar los datos
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Datos de ejemplo')
plt.show()

# Ajuste lineal utilizando el método de mínimos cuadrados
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Imprimir los resultados del ajuste lineal
print(f"Pendiente (m): {m}")
print(f"Intercepto (c): {c}")

# Graficar la línea de ajuste
plt.scatter(x, y)
plt.plot(x, m * x + c, 'r', label='Ajuste lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ajuste lineal de los datos')
plt.legend()
plt.show()
