#Menu limitado - Emmanuel Navarro 
print("Hola, bienvenido al menu de selección: ¿Qué quieres hacer?")
print("Moda, Multimodalidad, Moda texto, Salir")
print("Moda: Calcula la moda de una serie de números")
print("Multimodalidad: Calcula los números con la moda mayor en una serie de números")
print("Moda texto: Calcula la moda de las letras de un archivo de texto")
print("Salir: Salir del programa")

#Limitador de opciones
Correct = False
while Correct == False:
    entrada = input("Opción elegida es=")
    if entrada == 'Moda' or entrada == 'Multimodalidad' or entrada == 'Moda texto' or entrada=='Salir':
        #Lo que hace es comparar si la opción que ingresaste es uan de las opciones que pusiste
        Correct=True #Si es cierto, permite al programa avanzar
    else: #Si no, lo detiene y no lo deja avanzar
        print("La opción ingresada no existe, por favor intente otra vez..")

#Producción de las opciones
#Moda mayor del número
if entrada=='Moda':
    Num=True
    while Num==True: 
        try:
            cantidad=int(input("Por favor ingrese una cantidad de números que vas a ingresar="))
            Num=False
            pass
        except ValueError:
            print("Lo que ingreso no es un valor numérico, por favor ingrese un valor numérico")
    print(f"Su cantidad de números es de {cantidad}")
    #Ingresar cantidad de números
    Números = []
    i = 0
    while i < cantidad:
        try:
            número = int(input("Ingresar número"))
            Números.append(número)
            i=i+1
        except ValueError:
            print("No es un número")
        print(Números)
    #Ver el número que más se repite
    Mayor=0
    Repetido = 0
    Moda=0
    for i in range (0, cantidad):
        elemento = Números[i]
        Evaluar = Números.count(elemento)
        if Evaluar > Repetido:
            Repetido = Evaluar
            Moda = elemento
        if elemento > Mayor:
            Mayor=elemento
    print(f"Su moda es el número {Moda} y el número mayor es {Mayor}")    
    exit()

#Varios números con misma moda
if entrada=='Multimodalidad':
    Num=True
    while Num==True: 
        try:
            cantidad=int(input("Por favor ingrese una cantidad de números que vas a ingresar="))
            Num=False
            pass
        except ValueError:
            print("Lo que ingreso no es un valor numérico, por favor ingrese un valor numérico")
    print(f"Su cantidad de números es de {cantidad}")
    #Ingresar cantidad de números
    Números = []
    i = 0
    while i < cantidad:
        try:
            número = int(input("Ingresar número"))
            Números.append(número)
            i=i+1
        except ValueError:
            print("No es un número")
        print(Números)
    #Ver los números mayores que se repiten
    Mayor=0
    Repetido = 0
    Modas= []
    Moda = 0
    Repeticiones = 0
    for i in range (0, cantidad): #Determinar la moda que se repite
        elemento = Números[i]
        Evaluar = Números.count(elemento)
        if Evaluar > Repetido:
            Repetido = Evaluar
    for i in range (0, cantidad): #Ver que números repiten la moda
        elemento = Números[i]
        Repeticiones = Números.count(elemento)
        if Repeticiones==Repetido:
            Modas.append(elemento)
            presencia=Modas.count(elemento)
            if presencia > 1:
                Modas.remove(elemento)
    print(f"Las multimodalidades son {Modas}")    
    exit()

#Lectura del texto
if entrada=='Moda texto':
    archivo = open("Chimichanga.txt") 
    texto = archivo.readlines() 
    lista_letras = []
    for linea in texto:
        for i in range(len(linea)):
            elemento=lista_letras.append(linea[i]) 
    #Lectura de la cantidad de cada letra en todo el texto   
    a_f=lista_letras.count('a')
    print(f"La frecuencia de a es {a_f}")
    b_f=lista_letras.count('b')
    print(f"La frecuencia de b es {b_f}")
    c_f=lista_letras.count('c')
    print(f"La frecuencia de c es {c_f}")
    d_f=lista_letras.count('d')
    print(f"La frecuencia de d es {d_f}")
    e_f=lista_letras.count('e')
    print(f"La frecuencia de e es {e_f}")
    f_f=lista_letras.count('f')
    print(f"La frecuencia de f es {f_f}")
    g_f=lista_letras.count('g')
    print(f"La frecuencia de g es {g_f}")
    h_f=lista_letras.count('h')
    print(f"La frecuencia de h es {h_f}")
    i_f=lista_letras.count('i')
    print(f"La frecuencia de i es {i_f}")
    j_f=lista_letras.count('j')
    print(f"La frecuencia de j es {j_f}")
    k_f=lista_letras.count('k')
    print(f"La frecuencia de k es {k_f}")
    l_f=lista_letras.count('l')
    print(f"La frecuencia de l es {l_f}")
    m_f=lista_letras.count('m')
    print(f"La frecuencia de m es {m_f}")
    n_f=lista_letras.count('n')
    print(f"La frecuencia de n es {n_f}")
    ñ_f=lista_letras.count('Ã')
    print(f"La frecuencia de ñ es {ñ_f}")
    o_f=lista_letras.count('o')
    print(f"La frecuencia de o es {o_f}")
    p_f=lista_letras.count('p')
    print(f"La frecuencia de p es {p_f}")
    q_f=lista_letras.count('q')
    print(f"La frecuencia de q es {q_f}")
    r_f=lista_letras.count('r')
    print(f"La frecuencia de r es {r_f}")
    s_f=lista_letras.count('s')
    print(f"La frecuencia de s es {s_f}")
    t_f=lista_letras.count('t')
    print(f"La frecuencia de t es {t_f}")
    u_f=lista_letras.count('u')
    print(f"La frecuencia de u es {u_f}")
    v_f=lista_letras.count('v')
    print(f"La frecuencia de v es {v_f}")
    w_f=lista_letras.count('w')
    print(f"La frecuencia de w es {w_f}")
    x_f=lista_letras.count('x')
    print(f"La frecuencia de x es {x_f}")
    y_f=lista_letras.count('y')
    print(f"La frecuencia de y es {y_f}")
    z_f=lista_letras.count('z')
    print(f"La frecuencia de z es {z_f}")
    #Conteo de ñ
    ñ_f=lista_letras.count('Ã')
    a_f=lista_letras.count('±')

#Lectura de texto con lista 
if entrada=='Moda texto':
    archivo = open("Chimichanga.txt") 
    texto = archivo.readlines() 
    lista_letras = []
    for linea in texto:
        for i in range(len(linea)):
            elemento=lista_letras.append(linea[i]) 
    abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','Ã','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0, len(abecedario)-1):
        letra = abecedario[i]
        repeticion=lista_letras.count(letra)
        print(f"La frecuencia de {letra} es {repeticion}")
    exit()

#Salida del programa
if entrada=='Salir':
    print("Que tenga buen día :D")
    exit()