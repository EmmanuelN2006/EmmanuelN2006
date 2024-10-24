import numpy as np
import matplotlib.pyplot as plt

# Función para generar un vector unitario aleatorio
def generar_vector_unitario():
    # Generamos un ángulo aleatorio entre 0 y 2π
    angulo = np.random.uniform(0, 2 * np.pi)
    # Las componentes del vector unitario
    ux = np.cos(angulo)
    uy = np.sin(angulo)
    return np.array([ux, uy])

# Función para calcular la proyección de un vector v sobre otro vector u
def proyeccion(v, u):
    # La proyección es (v · u) / (u · u) * u, pero como u es unitario, simplificamos a (v · u) * u
    return (np.dot(v, u)) * u

# Función para graficar el vector original y sus proyecciones
def graficar_vectores(v, proy_u1, proy_u2, u1, u2):
    plt.figure()
    
    # Graficamos el vector original
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label="Vector Original")
    
    # Graficamos la proyección sobre el primer vector unitario
    plt.quiver(0, 0, proy_u1[0], proy_u1[1], angles='xy', scale_units='xy', scale=1, color='b', label="Proyección U1")

    # Graficamos la proyección sobre el segundo vector unitario
    plt.quiver(0, 0, proy_u2[0], proy_u2[1], angles='xy', scale_units='xy', scale=1, color='g', label="Proyección U2")
    
    # Graficamos los vectores unitarios
    plt.quiver(0, 0, u1[0], u1[1], angles='xy', scale_units='xy', scale=1, color='c', linestyle='dashed', label="Vector Unitario U1")
    plt.quiver(0, 0, u2[0], u2[1], angles='xy', scale_units='xy', scale=1, color='m', linestyle='dashed', label="Vector Unitario U2")

    # Configuración de la gráfica
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title("Proyección de un Vector sobre dos Vectores Unitarios")
    plt.show()

# Función principal
def main():
    while True:
        # Recibimos las componentes del vector
        x = float(input("Ingresa la componente en x del vector: "))
        y = float(input("Ingresa la componente en y del vector: "))
        
        # Creamos el vector a partir de las componentes
        vector = np.array([x, y])
        
        # Generamos dos vectores unitarios al azar
        u1 = generar_vector_unitario()
        u2 = generar_vector_unitario()

        # Calculamos las proyecciones del vector sobre los vectores unitarios
        proy_u1 = proyeccion(vector, u1)
        proy_u2 = proyeccion(vector, u2)

        # Mostramos los resultados
        print(f"Vector Original: {vector}")
        print(f"Proyección sobre U1: {proy_u1}")
        print(f"Proyección sobre U2: {proy_u2}")
        
        # Graficamos el vector original y las proyecciones
        graficar_vectores(vector, proy_u1, proy_u2, u1, u2)
        
        # Preguntamos si se quiere procesar otro vector
        continuar = input("¿Quieres ingresar otro vector? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
