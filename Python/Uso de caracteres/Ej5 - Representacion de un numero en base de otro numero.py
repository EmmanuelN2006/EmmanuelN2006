#Variables a utilizar
n=int #n es un número entero positivo
m=int #m es un número entero positivo menor a 10 y base del logaritmo
secuencia=int #Operacion para comparar los números que daría tal respuesta
i=float #Valores para comprobar si existe logaritmo de ese valor o n
resultado=float #Respuesta del logaritmo

#Introducir variables y verificar condiciones
print("Por favor, inserte un número entero positivo")
n=int(input())
if n<=0: #Aquí lo que hacemos es limitar el número ingresado del potenciado por las restricciones del logaritmo
    print("El número ingresado no es positivo")
    exit()
print("Ingrese un número entero positivo que sea menor que 10") #Condición que el número b sea menor que 10 pero debe ser entero y positivo
m=int(input())
if m<=0 or m>=10:
    print("El número ingresado no es positivo o no es menor que 10")
else:
    print("Se hará el cálculo de "+(str(n))+" en base "+(str(m)))

#Representación del logaritmo
def get_sub(x): #Para hacer la representación correctamente lo que se hace es usar el subíndice y esta es una forma de hacerlo
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)
#Definición y parte de código sacado de: "https://barcelonageeks.com/como-imprimir-superindice-y-subindice-en-python/#google_vignette"
#Hecho por Rudeus Greydat, 2022.

#Comandos del cálculo del logaritmo
for i in range (0, n+1, 1):
    resultado=int
    resultado=n/m**i #Al igual que la raíz, acá podremos hacer algo parecido, solo que cuando el resultado no es entero, usamos la libreria math
    if resultado==1:
        print('Log{}'.format(get_sub(str(m)))+(str(n))+" es "+(str(i)))
        exit()
    else:
        pass
    if i>=n: #Cosa que se demuestra aquí cuando el i ya es mayor que n o igual, ya que ese condicional respuesta se ha pasado del posible resultado
        print("El resultado no es un número entero")
        import math 
        print("El resultado original sería ")
        math.log(n,m)
        print('Log{}'.format(get_sub(str(m)))+(str(n))+" es "+(str(math.log(n,m))))
        exit()
    else:
        pass

#Podríamos agregar el comando de importar math que se encuentra abajo para cuando el resultado no es exacto y diga
#cuál es el valor original, sin embargo, el objetivo sería hacerlo con comandos

#Para probar logaritmos que no dan resultados en enteros y saber el resultado exacto si es que el resultado no es un entero
#import math 
#print("El resultado original sería ")
#math.log(n,m)
#print(math.log(n,m))
#Como en el ejercicio de la raiz cuadrada, podriamos usar el math para poder conocer el resultado exacto