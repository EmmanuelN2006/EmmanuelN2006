import numpy as np

# Definir la función
def f(x):
    return 1 / (1 + np.sqrt(x))**4

# Parámetros
a = 0
b = 1
n = 25
delta_x = (b - a) / n

# Crear los puntos de evaluación
x = np.linspace(a, b, n+1)

# Evaluar la función en los puntos
f_values = f(x)

# Aplicar la regla de Simpson
sum_impares = np.sum(f_values[1:-1:2])  # Suma de f(x_i) para i impares
sum_pares = np.sum(f_values[2:-2:2])   # Suma de f(x_i) para i pares

integral_approx = (delta_x / 3) * (f_values[0] + 4 * sum_impares + 2 * sum_pares + f_values[-1])

print(f'La aproximación de la integral es: {integral_approx}')
