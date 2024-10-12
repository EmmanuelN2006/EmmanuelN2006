#A partir de una función establecida, evaluar el área
print("A partir de x**2 + 3x + 1 se calcularán a partir de un número dado de particiones, entre mayor el número; mejor resultado")
n=int(input("Ingresar cantidad de particiones="))
print("Ahora debes poner dos números que serán los límites en los cuáles quieres calcular el área")
print("Por favor ingrese un valor A")
a=int(input("Valor de A="))
print("Por favor ingrese un valor B que sea mayor a A")
b=int(input("Valor de B="))

#N es el número de particiones, a y b son los límites de la función
#Determinar el número mayor
numerom=int
numeron=int
if a<b: #Determina los números mayores y menores
    numerom=b
    numeron=a
elif a>b:
    numerom=a
    numeron=b
else: #Si son iguales, el área será 0
    print("Los dos números son iguales, por favor que sean diferentes")
    print("Según propiedades de las integrales definidas, si los límites son iguales, la respuesta es 0")
    exit()

#Proceso de cálculo luego de comprobar
print("Sum.f(Xi)*DX=Área de la función")
i=int
DX=int #Diferencial de los valores en función a los datos ingresados
DX=((numerom-numeron)/n)
print(DX)

#Proceso de sumatoria
sumatoria=int
sumatoria=0
for i in range(1, n+1, 1):
    Xi=numeron+DX*i
    def f(Xi): #Función para definir el valor de un tal x en f(x)
        x=int
        x=Xi
        funcion=(x**2)+(3*x)+1
        print(funcion)
        return funcion
    sumatoria=sumatoria+f(Xi) #Proceso de la sumatoria
    print(sumatoria)
resultado=int
resultado=sumatoria*DX
print("El área de la función es= ")
print(resultado)