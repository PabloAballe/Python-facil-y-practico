
#importamos la biblioteca para abrir nuestro navegador
import webbrowser

#definimos en la funcion principal lo que  queremos imprimir en el nuevo fichero
def main():
    #le pasamos la ruta del fichero esta sera por defecto en la misma carpeta que se encuentra el programa de Python
    ruta = "index.html"
    #le decimos a python que as siguientes intrucciones las ponga dentro del fichero
    with open(ruta, mode="w", encoding="utf-8") as fichero:

        #aqui comienza nuestra web
        print("<!DOCTYPE html>", file=fichero)

        #especificamos el lenguaje
        print('<html lang="es">', file=fichero)
        print("<head>", file=fichero)
        print('  <meta charset="utf-8">', file=fichero)

        #especificamos el título
        print("  <title>Python Web</title>", file=fichero)
        print('  <meta name="viewport" content="width=device-width, initial-scale=1.0">',file=fichero)
        print("</head>", file=fichero)
        print("", file=fichero)
        print("<body>", file=fichero)

        #escribimos un parrafo inicial
        print("  <p>Estamos aprendiendo como desarrollar webs con Python</p>", file=fichero)

        #cerramos las etiquetas del cuerpo de nuestra web y el documento html
        print("</body>", file=fichero)
        print("</html>", file=fichero)


#le decimos a la libreria webbrowser que abra la ruta del fichero
    webbrowser.open(ruta)

#le decimos a python cual queremos que sea nuestra funcion de inicio
if __name__ == "__main__":
    main()
