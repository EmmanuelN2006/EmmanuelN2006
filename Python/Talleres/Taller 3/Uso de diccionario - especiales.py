#Chess Dictionary Validator - Funcion 1
#Fantasy Game Inventory - Funcion 2
#List to Dictionary Function for Fantasy Game Inventory -  Funcion 2

print("Hola! ¿Qué quieres hacer?"); print("Jugar Ajedrez, ver tu inventario de fantasía y pelear con un dragón para ganar loot")
Modo = input("= ").lower()
if Modo == "jugar ajedrez":
    ###Modalidad de ajedrez###
    print("Vamos a jugar ajedrez!")
    Fichas = ["Peón", "Torre", "Caballo", "Alfil", "Reina", "Rey"] #Recordatorio
    Colores = ["Blanco", "Negro"]
    Dimensiones_tabla = [8, 8]
    ## Establecer la tabla y jugador ##
    print("¿Qué equipo quieres ser?"); print("Blanco o Negro?")
    Equipo = input("= ").lower()
    if Equipo == "blanco":
        Izq_Der = ["A", "B", "C", "D", "E", "F", "G", "H"]
        Arr_Aba = ["1", "2", "3", "4", "5", "6", "7", "8"]       
    if Equipo == "negro":
        Izq_Der = ["A", "B", "C", "D", "E", "F", "G", "H"]
        Aba_Arr = ["8", "7", "6", "5", "4", "3", "2", "1"]