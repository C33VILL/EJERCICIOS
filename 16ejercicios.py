print ("16 EJERCICIOS")
##CENTENO VILLAVICENCIO URIEL 🐧 IRD42
print ("-------------numero1----------")
palabras = ["python","java","python","c++"]
veces={}
for wordd in palabras:
    if wordd in veces:
        veces[wordd]+=1
    else:
        veces[wordd]=1
    
print (veces)
#lista= [ element for element in palabras if element in veces: veces[element]+=1 else veces[element]=1 return veces]
   
print ("--------------->numero2-------->")

dic1={'a':1, 'b':2}
dic2={'b':3, 'c':4}
print (f"a:{dic1['a']},b:{dic1['b']+dic2['b']},c:{dic2['c']}")

print ("-------------numero3---------")
numeros=[1,1,2,3,3,3]
serepite={}
for numero in numeros:
    if numero in serepite:
        serepite[numero] +=1
    else:
         serepite[numero]=1
print (serepite) 

print ("----------numero4-------")
palabras =["hola", "mundo", "python", "programación"]
longitud =5
wordd=[palabra for palabra in palabras 
                if len(palabra)>=longitud]
print (wordd)

print ("---------numer5-------")
tuplas = [(1, 2), (3, 4), (5, 6)]
print (tuplas)
invertir=[ (b,a) for a,b in tuplas ]
print (invertir)

print ("----------------numero6-")
numeros = [1, 2, 3, 1, 2, 1]
moda = {}
for numer0 in numeros:
    if numer0 in moda:
        moda[numer0] += 1
    else:
        moda[numer0] = 1
morerepetido = max(moda, key=moda.get)
print(morerepetido)

print ("----------7")
conjunto1={1,2,3}
conjunto2={1,2,3,4,5}

conjunto_total=conjunto1.issubset(conjunto2)
print (conjunto_total)

print ("-------8")
personas = [{"nombre":"Ana", "edad": 25}, {"nombre": "Luis", "edad":25}, {"nombre": "Carlos", "edad": 30}]
salida={}
for persona in personas:
    edad=persona['edad']
    nombre=persona['nombre']
    if edad in personas:
        salida[edad].append(nombre)
    else:
        salida[edad]=[nombre]
print (salida)

print ('numero9')
#:(

print ('numero--10')
numeros=[1,2,3,4,5]
limite=3
filtro=[x for x in numeros if x >= limite]
print (filtro)

print ('numero 11---')
lista_de_listas = [[1, 2], [3, 4], [5]]
lista2=[]
for lista1 in lista_de_listas:
    for element in lista1:
        lista2.append(element)
print (lista2)


print("-------------------12")
numer=[1,2,3,4,5]
print(sum(numer)/5)


print ('---------------------------------13--')
numeros = [1, 2, 3]



print ("-------14")
frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
contar = {}
for i, frase in enumerate(frases):
    contar[i] = len(frase.split())
print(contar)



print ("15-----")
diccionario = {'a': 10, 'b': 20, 'c': 5}
maximo = max(diccionario, key=diccionario.get)
print(maximo)



print ('16----------')
#palíndromo
#nombre masculino
#Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo, anilina; dábale arroz a la zorra el abad.
palabras = ["ana", "oso", "hola", "level","anilina"]
palindromos = []
for palabra in palabras:
    if palabra == palabra[::-1]:
        palindromos.append(palabra)
print(palindromos)