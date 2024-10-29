import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math as mt

#Operaciones básicas entre dos números
print("Operaciones a utilizar; Suma, resta, multiplicación, división, potencia, raíz, log, sen, cos, tan, base 10")
#Para saber si cada operación usada está bien, utilizamos algo que llamaremos [Check]

#Operaciones
def suma(): #Operación de la suma
    elemento1 = print("Hola")
    Ventana_suma = tk.Tk(); Ventana_suma.geometry("640x480"); Ventana_suma.resizable(False, False)
    Ventana_suma.title("Suma python")
    texto= tk.Label(Ventana_suma, text="Hola"); texto.place(x=320, y=240)
    Ventana_suma.mainloop()
    return elemento1

#Interfaz gráfica
#Configuración de la ventana y sus propiedades
Ventana = tk.Tk() #Tk() - Mantiene la ventana siempre abierta
Ventana.title("Pythuladora") #Nombre de la ventana
Ventana.geometry("640x480") #Resolución original o primera vez que habras la ventana
Ventana.resizable(False, False) #Si a la ventana se le puede aumentar o disminuir la resolución por algún lado

boton_suma = tk.Button( Ventana, text="Suma", bd=4, command=suma); boton_suma.place(x=320, y=240) #Función y lugar

Ventana.mainloop() #Carga los elementos de la interfaz gráfica y los muestra