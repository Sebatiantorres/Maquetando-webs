# Aca va un comentario
if 5 > 3:
# Aca va un comentario
 #   print("5 es mayor a 3")
    x = 5
    y = "chanchito feliz"


#print(x, y)

email = "chanchito@feliz.com"
_mivar_ = "chanchito"

MIVAR = "CHANCHITO"
a, b, c = "Lala", "Lele", "Lili"

#print(_mivar_, "    ", MIVAR, "    ", a, b, c)

valor1 = valor2 = valor3 = "CHANCHITO FELIZ"

#print(valor1, valor2, valor3)

inicio = "Hola"
final = "mundo"
#print(inicio + final)

palabra = "Hola mundo" #string
palabra1 = 'Hola mundo' #string

entero = 20 #integer
conDecimal = 20.2 #float
complejo = 1j

#print(palabra, palabra1, entero, conDecimal, complejo)
#listas
lista = ["hola", "Mundo", "CHANCHITO FELIZ"]
lista2 = lista.copy()
lista.append("j")
#lista.clear()
#lista.pop()  #este elimina el ultimo elemento de la lista
#lista.remove("hola") #este elimina un elemento por su valor
lista.reverse()
lista.sort()
tupla = ("hola", "mundo", "somos", "tupla")
listaDeTupla = list(tupla)

listaDeTupla.append("Chanchito")
#print(listaDeTupla)

rango = range(6)
#print(rango)

diccionario = {
    "nombre": "chanchito feliz",
    "raza": "Persa",
    "edad": 5
}

#print(diccionario["raza"])
#print(diccionario.get("nombre"))
diccionario["nombre"] = "Fluffy"
print(diccionario)

diccionario["ronronea"]="Si"