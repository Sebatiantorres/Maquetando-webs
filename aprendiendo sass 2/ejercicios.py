"""
dato = input("ingrese dato: ")

lista = ["hola", "mundo", "chanchito", "feliz", "dragones"]

if lista.count(dato) > 0:
    print("el dato existe", dato)
else:
    print("el dato no existe", dato)
"""


primero = input("ingrese primer numero: ")
try:
    primero = int(primero)
except:
    primero = "chanchito feliz"
if primero == "chanchito feliz":
    print("el valor ingresado no es un entero")
    exit()


segundo = input("ingrese segundo numero: ")
try:
    segundo = int(segundo)
except:
    segundo = "chanchito feliz"
if segundo == "chanchito feliz":
    print("el valor ingresado no es un entero")
    exit()
simbolo = input("ingrese el simbolo: ")
if simbolo == "+":
    print("Suma", primero + segundo)
elif simbolo == "-":
    print("Resta", primero - segundo)
elif simbolo == "*":
    print("Multiplicacion", primero * segundo)
elif simbolo == "/":
    print("Division", primero / segundo)
else:
    print("el simbolo ingresado no es valido")
