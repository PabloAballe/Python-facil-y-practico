#juego de dados para dos jugadores

#importamos la random

from random import randrange




#Mensaje de bienvenida
print("Bienvenido a Dados Python")

#determinamos un ganador
ganador=0
bot_ganador=0
nombre_ganador=""
numero_bot=0
n_bots=0

#pedimos el numero de jugadores
n_jugadores=int(input("¿Cuantos jugadores humanos van a jugar ?: "))
bots=input("¿Quieres jugar con algunos bots?: ")

#convertimos las respuestas a minusculas para prevenir errores

if bots.lower()=="si":
    n_bots=int(input("Con cuantos bots quieres jugar?: "))

if n_jugadores>1 and n_bots==0:

    for i in range(1,n_jugadores+1):
        jugador=input(f"¿Cual es el nombre del jugador {i}?: ")
        dado=randrange(1,7)
        print(f"El jugador {jugador} ha jugado {dado}")


        if dado>ganador:
            ganador=dado
            nombre_ganador=jugador
    print(f"El ganador es {nombre_ganador} que ha sacado un {ganador}")

else:


#bosts
    for i in range(1,n_bots+1):
        dado=randrange(1,7)
        bot=print(f"El bot {i} a jugado {dado}")

        if dado>ganador:
            bot_ganador=dado
            numero_bot=i

    #jugadores humanos
    for i in range(1,n_jugadores+1):
        jugador=input(f"¿Cual es el nombre del jugador {i}?: ")
        dado=randrange(1,7)
        print(f"El jugador {jugador} ha jugado {dado}")


    if numero_bot>0 and bot_ganador>ganador:
        print(f"Ha ganado el bot  número {numero_bot} con un {bot_ganador}")
    else:
        print(f"El ganador es {nombre_ganador} que ha sacado un {ganador}")


#despedida
print("Hasta la proxima, gracias por jugar")
