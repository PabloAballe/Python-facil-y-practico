
#importamos la libreria
from tkinter import *
from tkinter import messagebox

window = Tk()

#titulo
window.title("Bienvenido a Python")


#establecemos el tamaño de la ventana
window.geometry('800x600')

#aqui esta nuestro texto
lbl = Label(window, text="¿Cual es tu nombre?", fg="blue")



#definimos la funcion que maneja el Clic
def clic():
    nombre=f"Bienvenido {txt.get()}"
    lbl.configure(text=nombre)

    messagebox.showerror('Desde Tkinter','Gracias por usar Python')

#campo de entrada de texto
txt = Entry(window,width=10)
txt.grid(column=0, row=1)

#establecemos nuestro boton
btn = Button(window, text="Dame clic", bg="blue", fg="white", command=clic)



btn.grid(column=1, row=0)

lbl.grid(column=0, row=0)


#bucle principal de nuestra aplicación
window.mainloop()
