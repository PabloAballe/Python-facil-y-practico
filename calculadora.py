#calculadora en Python


#bienvenida
print("Bienvenido a mi Calculadora en Python")
print("Para comenzar sigue los pasos que se te piden a continuación: ")



#valores de el usuario
numero1=int(input("Escribe el primer número: "))
numero2=int(input("Escribe el segundo número: "))

#menu
print("Las opciones disponibles son: ")
print()
print("1-Suma")
print("2-Resta")
print("3-Multiplicación")
print("4-Division")
print("5-Exponete")
print("6-Modulo")
print()
print()
operacion=int(input("¿Que operación quieres realizar?(escribe el número): "))






# sumar
def suma(numero1, numero2):
    suma=numero1+numero2
    print(f"La suma de tus números es: {suma}")

# restar
def restar(numero1, numero2):
    resta= numero1-numero2
    print(f"La resta de tus números es la siguiente: {resta}")

#multiplicacion

def multiplicar(numero1, numero2):
    multiplicacion= numero1*numero2
    print(f"El resultado de la multiplicacion de tus números es el siguiente: {multiplicacion}")

#division
def dividir(numero1,numero2):
    division=numero1/numero2
    print(f"El resultado de la división de tus números es el siguiente: {division}")

# exponente

def exponente(numero1, numero2):
    exponente=numero1**numero2
    print(f"El exponte de tus operandos es: {exponente}")

# modulo
def modulo(numero1, numero2):
    resto=numero1%numero2
    print(f"El resto de tus numeros es: {resto}")


#manejamos la operacion a realizar

if operacion==1:
    suma(numero1,numero2)
elif operacion==2:
    resta(numero1,numero2)
elif operacion==3:
    multiplicar(numero1,numero2)
elif operacion==4:
    dividir(numero1, numero2)
elif operacion==5:
    exponente(numero1, numero2)
elif operacion==6:
    modulo(numero1,numero2)
else:
    print("Ha ocurrido un error inesperado")

while operacion>6 or operacion<1:
    print("Porfavor escriba una opcion válida ")
    #menu
    print("Las opciones disponibles son: ")
    print()
    print("1-Suma")
    print("2-Resta")
    print("3-Multiplicación")
    print("4-Division")
    print("5-Exponete")
    print("6-Modulo")
    print()
    print()
    operacion=int(input("¿Que operación quieres realizar?(escribe el número): "))
