Detener = bool; Detener = False

while not Detener:
    Numero = input("Ingrese un número a convertir= ") #Número a ingresar
    if int(Numero) <=0:
        print("Deteniendo el programa")
        Detener = True
        exit()

    Largo = len(Numero) #Cantidad de elementos para dividir
    if Largo > 5:
        print("Número demasiado grande")
        Detener = True
        exit()
    
    #########Diccionario###########
    Unidades = {'0':'','1':'I', '2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
    Decenas = {'10':'X','20':'XX','30':'XXX','40':'XL','50':'L','60':'LX','70':'LXX','80':'LXXX', '90':'XC'}
    Centenas = {'100':'C','200':'CC','300':'CCC','400':'CD','500':'D','600':'DC','700':'DCC','800':'DCCC', '900':'CM'}
    Millares = {'1000':'M','2000':'MM','3000':'MMM','4000':'IV-','5000':'V-','6000':'VI-','7000':'VII-','8000':'VIII-', '9000':'IX-'}
    Decenas_millares = {'10000':'X-', '20000':'XX-', '30000':'XXX-','40000':'XL-','50000':'L-','60000':'LX-','70000':'LXX-','80000':'LXXX-', '90000':'XC-'}
    ########Diccionario############

    Cifras = []

    ##Organización de los números
    if Largo == 1:
        Unidad = Numero
        Resultado = Unidades[Numero]
        print(Resultado)
    if Largo == 2:
        Unidad = Numero[1]
        Decena = str(int(Numero[0])*10)
        Resultado = Decenas[Decena] + Unidades[Unidad]
        print(Resultado)
    if Largo == 3:
        Unidad = Numero[2]
        Decena = str(int(Numero[1])*10)
        Centena = str(int(Numero[0])*100)
        Resultado = Centenas[Centena] + Decenas[Decena] + Unidades[Unidad]
        print(Resultado)
    if Largo == 4:
        Unidad = Numero[3]
        Decena = str(int(Numero[2])*10)
        Centena = str(int(Numero[1])*100)
        Millar = str(int(Numero[0])*1000)
        Resultado = Millares[Millar] + Centenas[Centena] + Decenas[Decena] + Unidades[Unidad]
        print(Resultado)
    if Largo == 5:
        Unidad = Numero[4]
        Decena = str(int(Numero[3])*10)
        Centena = str(int(Numero[2])*100)
        Millar = str(int(Numero[1])*1000)
        Decena_millar = str(int(Numero[0])*10000)
        Resultado = Decenas_millares[Decena_millar] + Millares[Millar] + Centenas[Centena] + Decenas[Decena] + Unidades[Unidad]
        print(Resultado)