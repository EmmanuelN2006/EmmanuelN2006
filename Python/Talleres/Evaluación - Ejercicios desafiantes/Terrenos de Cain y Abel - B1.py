# Página del ejercicio: https://aceptaelreto.com/problem/statement.php?id=103&cat=13

Ingresando = True

print("Vamos a evaluar la función ax³ + bx² + cx + d; si quiere salir, escribir 20, sino otra cosa")

while Ingresando:
    #### Ingreso de las variables ###
    Error = False
    Decisión = input("Ingresar= ") 
    if Decisión == '20':  # Por si se quiere salir
        Ingresando = False
        break

    print("El grado debe ser del rango [0, 19]")
    try:
        Grado = int(input("Grado del polinomio: "))  # Determina el grado a partir de la entrada del usuario
        if Grado < 0 or Grado > 19:
            print("El grado sale del rango")
            Error = True
    except ValueError:
        print("El valor ingresado no es compatible")
        Error = True

    try:
        Elementos = input("Coeficientes en orden decreciente (ej. 1 2 -1 0): ").split()
        Coeficientes = list(map(int, Elementos))  # Convertir todos los coeficientes a enteros
        if len(Coeficientes) != Grado + 1:  # Asegurar que la cantidad de coeficientes corresponde al grado
            print("Número de coeficientes no corresponde con el grado")
            Error = True
    except ValueError:
        print("El valor ingresado no es compatible")
        Error = True
    
    try:
        print("Número de rectángulos")
        N_Rectangulos = int(input("= "))
        if N_Rectangulos <= 0:
            print("El número ingresado no es válido")
            Error = True
    except ValueError:
        print("El valor ingresado no es compatible")
        Error = True
    ##############################
    if not Error:
        # Definir y llamar a la función de cálculo
        def calcular_terreno(grado, coeficientes, n_rectangulos):
            umbral = 0.001  # Tolerancia para determinar si el reparto es justo
            base = 1 / n_rectangulos  # Ancho de cada rectángulo
            area_cain = 0
            # Función que evalúa el polinomio en un valor x
            def f(x):
                return sum(coeficientes[i] * x**(grado - i) for i in range(grado + 1))
            # Cálculo del área usando sumas de Riemann
            for i in range(n_rectangulos):
                x_i = i * base
                altura = f(x_i)
                
                # Ajuste de altura para los límites del terreno
                if altura < 0:
                    altura = 0
                elif altura > 1:
                    altura = 1
                area_cain += altura * base  # Área de cada rectángulo en la sumatoria
            # Área de Abel es el área complementaria
            area_abel = 1 - area_cain
            diferencia = abs(area_cain - area_abel)
            # Determinación del resultado basado en la diferencia
            if diferencia <= umbral:
                return "JUSTO"
            elif area_cain > area_abel:
                return "CAIN"
            else:
                return "ABEL"
        # Llamar a la función y mostrar el resultado
        resultado = calcular_terreno(Grado, Coeficientes, N_Rectangulos)
        print("Resultado:", resultado)
    else:
        print("Hubo un error en la entrada. Por favor, intente de nuevo.")

    # Preguntar si se desea ingresar otro caso
    continuar = input("¿Desea ingresar otro caso? (s/n): ").lower() #Obliga al input a convertirse en minusculas 
    if continuar != 's':
        Ingresando = False
