#cálculo del dia de la semana en Python


#bienvenida
print("Programa para cálcular el dia de la semana")


#pedimos los datos al usuario
dia=int(input("Dime un numero de días: "))
mes=int(input("Ahora dime el mes: "))
ano=int(input("¿Y en que año?: "))


#añadirmos las variables
a=(14-mes)//12
b=ano-a
c=mes+(a*12)-2
d=b//4
e=b//100
f=b//400
g=(31*c)//12
h=dia+b+d-e+f+g
i=h%7


if i==0:
    print("¡El dia cae Domingo!")
elif i==1:
    print("¡El dia cae Lunes!")
elif i==2:
    print("¡El dia cae Martes!")
elif i==3:
    print("¡El dia cae Miércoles!")
elif i==4:
    print("¡El dia cae Jueves!")
elif i==5:
    print("¡El dia cae Viernes!")
elif i==6:
    print("¡El dia cae Sábado!")
else:
    print("Ha ocurrido un error inesperado")


print("¡Hasta la próxima!")
