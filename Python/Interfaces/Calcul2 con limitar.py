#Interfaz para calcular sumas, restas, multiplicaciones, divisiones, potencias y raices
import tkinter as tk
vacio = ''

def sumar():
    try: #Intenta ejercer la operación
        operando1 = texto1.get()
        operando2 = texto2.get()
        resultado = float(operando1) + float(operando2) #Si algún valor no puede convertirse en número = error
        print(resultado)
        textof.configure(state=tk.NORMAL)
        textof.delete(0, tk.END)
        textof.insert(0, resultado)
        textof.configure(state=tk.DISABLED)
    except ValueError: #Cuando se active error en "resultado = operando1+operando2" dará la secuencia:
        print("Error en la suma, un valor no es numérico") #Imprime esto en la consola
        resultado = 'Error'
        print(resultado) #Imprime esto en la consola
        textof.configure(state=tk.NORMAL)
        textof.delete(0, tk.END)
        textof.insert(0, resultado) #Imprime esto en las casillas 
        textof.configure(state=tk.DISABLED)

def restar():
    try: #Intenta ejercer la operación
        operando1 = texto1.get()
        operando2 = texto2.get()
        resultado = float(operando1) - float(operando2) #Si algún valor no puede convertirse en número = error
        print(resultado)
        textof.configure(state=tk.NORMAL)
        textof.delete(0, tk.END)
        textof.insert(0, resultado)
        textof.configure(state=tk.DISABLED)
    except ValueError: #Cuando se active error en "resultado = operando1+operando2" dará la secuencia:
        print("Error en la resta, un valor no es numérico") #Imprime esto en la consola
        resultado = 'Error'
        print(resultado) #Imprime esto en la consola
        textof.configure(state=tk.NORMAL)
        textof.delete(0, tk.END)
        textof.insert(0, resultado) #Imprime esto en las casillas 
        textof.configure(state=tk.DISABLED)

def multiplicar():
    try: #Intenta ejercer la operación
        operando1 = texto1.get()
        operando2 = texto2.get()
        resultado = float(operando1) * float(operando2) #Si algún valor no puede convertirse en número = error
        print(resultado)
        textof.configure(state=tk.NORMAL)
        textof.delete(0, tk.END)
        textof.insert(0, resultado)
        textof.configure(state=tk.DISABLED)
    except ValueError: #Cuando se active error en "resultado = operando1+operando2" dará la secuencia:
        print("Error en la multiplicación, un valor no es numérico") #Imprime esto en la consola
        resultado = 'Error'
        print(resultado) #Imprime esto en la consola
        textof.configure(state=tk.NORMAL)
        textof.delete(0, tk.END)
        textof.insert(0, resultado) #Imprime esto en las casillas 
        textof.configure(state=tk.DISABLED)

def dividir(): #Restricción del cero - Hecho
    try: #Intenta ejercer la operación
        operando1 = texto1.get() #Dividiendo
        operando2 = texto2.get() #Divisor
        if float(operando2)==0: #Si al comparar el operando2, este es 0
            print("El divisor es 0, cambiar el divisor") #Obliga al usuario a cambiarlo
            texto2.configure(state=tk.NORMAL) #Permite el cambiar al código
            texto2.delete(0, tk.END) #Borra el operando2
            texto2.insert(0, vacio) #Pone espacio en el operando2
            textof.configure(state=tk.NORMAL) #Permite el cambiar al código
            textof.delete(0, tk.END) #Borra el resultado
            textof.insert(0, "Error") #Reemplaza el espacio de resultado por Error
            textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado
        else:
            resultado = float(operando1) / float(operando2) #Si algún valor no puede convertirse en número = error
            print(resultado)
            textof.configure(state=tk.NORMAL) #Permite el cambiar al código
            textof.delete(0, tk.END) #Borra el resultado
            textof.insert(0, resultado) #Reemplaza el espacio de resultado por la respuesta
            textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado
    except ValueError: #Cuando se active error en "resultado = operando1+operando2" dará la secuencia:
        print("Error en la división, el valor no es númerico") #Imprime esto en la consola
        resultado = 'Error'
        print(resultado) #Imprime esto en la consola
        textof.configure(state=tk.NORMAL) #Permite el cambiar al código
        textof.delete(0, tk.END) #Borra el resultado
        textof.insert(0, resultado) #Reemplaza el espacio de resultado por la respuesta
        textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado

def potencia(): #Restricción del cero elevado a la cero - Hecho
    try: #Intenta ejercer la operación
        operando1 = texto1.get() #Base
        operando2 = texto2.get() #Exponente
        if float(operando2)==0: #Cuando el exponente es 0
            if float(operando1)==0: #Cuando la base es 0
                print("La base, operando1, no puede ser 0 si el exponente es 0") #Obliga al usuario a cambiarlo
                texto1.configure(state=tk.NORMAL) #Permite el cambiar al código
                texto1.delete(0, tk.END) #Borra el operando1
                texto1.insert(0, vacio) #Pone espacio en el operando1
                textof.configure(state=tk.NORMAL) #Permite el cambiar al código
                textof.delete(0, tk.END) #Borra el resultado
                textof.insert(0, "Error") #Reemplaza el espacio de resultado por Error
                textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado   
            else:
                resultado = float(operando1) ** float(operando2) #Si algún valor no puede convertirse en número = error
                print(resultado)
                textof.configure(state=tk.NORMAL) #Permite el cambiar al código
                textof.delete(0, tk.END) #Borra el resultado
                textof.insert(0, resultado) #Reemplaza el espacio de resultado por el verdadero resultado
                textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado
        if float(operando2)!=0: #Cuando el exponente es diferente de 0
            resultado = float(operando1) ** float(operando2) #Si algún valor no puede convertirse en número = error
            print(resultado)
            textof.configure(state=tk.NORMAL) #Permite el cambiar al código
            textof.delete(0, tk.END) #Borra el resultado
            textof.insert(0, resultado) #Reemplaza el espacio de resultado por el verdadero resultado
            textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado
    except ValueError: #Cuando se active error en "resultado = operando1+operando2" dará la secuencia:
        print("Error en la potencia, un valor no es numérico") #Imprime esto en la consola
        resultado = 'Error'
        print(resultado) #Imprime esto en la consola
        textof.configure(state=tk.NORMAL) #Permite el cambiar al código
        textof.delete(0, tk.END) #Borra el resultado
        textof.insert(0, resultado) #Reemplaza el espacio de resultado por el verdadero resultado
        textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado

def radicacion(): #Restricción de exponente 0 excepto raiz cero de 0 - Trabajar
    try: #Intenta ejercer la operación
        operando1 = texto1.get() #Potencia
        operando2 = texto2.get() #Grado de la raíz
        if float(operando2)==0: #Cuando la raíz esta elevada a la cero
            if float(operando1)==0: #Cuando la potencia es 0
                print("0")
                textof.configure(state=tk.NORMAL) #Permite el cambiar al código
                textof.delete(0, tk.END) #Borra el resultado
                textof.insert(0, "0") #Reemplaza el espacio de resultado por 0
                textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado 
            else:
                print("La potencia debe ser igual a 0 cuando esta en raíz cero") #Obliga al usuario a cambiarlo
                print("De lo contrario, cambia el exponente")
                texto1.configure(state=tk.NORMAL) #Permite el cambiar al código
                texto1.delete(0, tk.END) #Borra el operando1
                texto1.insert(0, vacio) #Pone espacio en el operando1
                textof.configure(state=tk.NORMAL) #Permite el cambiar al código
                textof.delete(0, tk.END) #Borra el resultado
                textof.insert(0, "Error") #Reemplaza el espacio de resultado por Error
                textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado 
        if float(operando2)!=0: #Cuando la raíz no está elevada a la 0
            resultado = float(operando1) ** (1/(float(operando2))) #Si algún valor no puede convertirse en número = error
            print(resultado)
            textof.configure(state=tk.NORMAL)  #Permite el cambiar al código
            textof.delete(0, tk.END) #Borra el resultado
            textof.insert(0, resultado) #Reemplaza el espacio de resultado por el resultado verdadero
            textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado 
    except ValueError: #Cuando se active error en "resultado = raiz operando 2 en operando1" dará la secuencia:
        print("Error en la raíz, un valor no es numérico") #Imprime esto en la consola
        resultado = 'Error'
        print(resultado) #Imprime esto en la consola
        textof.configure(state=tk.NORMAL)  #Permite el cambiar al código
        textof.delete(0, tk.END) #Borra el resultado
        textof.insert(0, resultado) #Reemplaza el espacio de resultado por el resultado verdadero
        textof.configure(state=tk.DISABLED) #Desactiva el cambio del resultado 

ventana = tk.Tk()

ventana.title("Kalculadora")
ventana.geometry('640x480')
ventana.resizable(False, False)

texto1 = tk.Entry( ventana, width=20)
texto2 = tk.Entry( ventana, width=20)
textof = tk.Entry( ventana, width=20, state="disabled")

etiqueta1 = tk.Label(ventana, text="Operando 1:")
etiqueta2 = tk.Label(ventana, text="Operando 2:")
etiquetaf = tk.Label(ventana, text="Resultado:")

boton_suma = tk.Button( ventana, text="+", bd = 3, command=sumar)
boton_resta = tk.Button( ventana, text="-", bd = 3, command=restar)
boton_producto = tk.Button( ventana, text="*", bd = 3, command=multiplicar)
boton_cociente = tk.Button( ventana, text="/", bd = 3, command=dividir)
boton_potencia = tk.Button( ventana, text='x^y', bd = 3, command=potencia)
boton_radicacion = tk.Button( ventana, text='Raiz', bd = 3, command=radicacion)
boton_salir = tk.Button( ventana, text="salir", bd=2, command=ventana.destroy)

texto1.place(x=100, y=100)
texto2.place(x=100, y=200)
textof.place(x=100, y=300)

etiqueta1.place(x=200, y=100)
etiqueta2.place(x=200, y=200)
etiquetaf.place(x=200, y=300)

boton_suma.place(x=400, y=100)
boton_resta.place(x=450, y=100)
boton_producto.place(x=400, y=200)
boton_cociente.place(x=450, y=200)
boton_potencia.place(x=400, y=300)
boton_radicacion.place(x=450, y=300)

boton_salir.pack(anchor="center", side="bottom")

ventana.mainloop()
