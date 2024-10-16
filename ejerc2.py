###numero 1
a=0
b=50 
suma=a+b
print (suma)

#2
cadena1="google"
cadena2="cloud"
cadena3= cadena1,cadena2
print(f"{cadena3}")

##3
print("areaa de rectangulo")
base=7
altura=7
area=base*altura
print(area)

##4
num=4
div=num%2
if div == 0:
    print("par")
else:
    print ("impar")


##5
num=5
for num in range (-1):
    num+=1
    print (num)
print(num)


##6
lista=[100,250,90,350,190]
grande=max(lista)
print(grande)

##7
celsius = 100
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)  

##8
num=20
div=num/5
if div == 1:
    print (True)
else:
    print (False)


##9
cadena="banana"
caracter="n"
veces=cadena.find("n")
print(veces)

##10
lista=[5, -5, 10, -10]
suma= sum(lista)
print(suma)

##11
inicio=0
fin=5
for p in range(0,6):
    if p%2==0:
        print(f'{p}')
    else:
        None

##12
lista=[5, 10]
promedio1=sum(lista)
promedio2=promedio1/2
print(promedio2)

##13
###############################################
cadena = "Examen"
resultado = cadena[::-1]
print(resultado)
##14
lista=[1,2,3,-10,4]
minim=min(lista)
print(minim)

##15
palabra = "mundo"
resultado = palabra == palabra[::-1]
print(resultado)
#########################################################
##16

oracion="!hola¡"
wordss=oracion.count("!")
print(wordss)

##17
base=7
exponente=4
Re= base**exponente
print(Re)

##18
kilometros =1
milla=1.609344
salida=kilometros/milla
print (salida)

##19
lista=[0, -1, -2]
lista2 = [ e * e for e in lista]
print(lista2)

##20
lista=[0, -1, -5, -3]
print(sorted(lista))


##21
lista=[]
valores=lista.count('')
print(valores)

##22
numero = 101
suma_digitos = sum(int(digit) for digit in str(numero))
print(suma_digitos)
#######################################



##23
cadena="examen"
cadenaM=cadena.upper()
print(cadenaM)

###24
lista=[100,50,50,25,100]

##25
cadena="abracadabra"
ca=cadena.count('a')
print(ca)
##26
n=3

##27
cadena="Open ai"
cade=cadena.replace(" ", "")
print(cade)

##28
inicio=15
fin=25
for h in range (15,26):
    if h%2==1:
        h+=1
        print(h)
    else:
        None


#29
diccionario = {"rojo": "red", "verde": "green"}
invertido = {values: key  for key, values in diccionario.items()}
print(invertido)

##3000
lista = [100, 200, 300, 400, 500, 600]
resultado = len(lista)
print(resultado) 


##31
diccionario = {5: "a", 15: "b", 25: "c"}
resultado = sum(diccionario.keys())
print(resultado)  

###32
lista = ["programar", "es", "genial"]
resultado = [cadena.upper() for cadena in lista]
print(resultado)
    
