
import re
from statistics import variance
import tkinter as tk
import random

dif = "Facil"
comando =""
def calcular():
    global comando
    if operacion.get() == 1:
        comando = "Suma"
        return comando
    elif operacion.get() == 2:
        comando = "Resta"
        return comando
    elif operacion.get() == 3:
        comando = "Multi"
        return comando
    elif operacion.get() == 4:
        comando = "Divi"
        return comando
def retornar(comando):
    global cantbuenos,cantjuegos,cantmalos
    resultado = valor.get()
    if comando == "Suma":
        if resultado == suma():
            cantbuenos.set(cantbuenos.get()+1)
        else:
            cantmalos.set(cantmalos.get()+1)
        cantjuegos.set(cantjuegos.get()+1)
    elif comando == "Resta":
        if resultado == restar():
            cantbuenos.set(cantbuenos.get()+1)
        else:
            cantmalos.set(cantmalos.get()+1)
        cantjuegos.set(cantjuegos.get()+1)

    elif comando == "Multi":
        if resultado == multi():
            cantbuenos.set(cantbuenos.get()+1)
        else:
            cantmalos.set(cantmalos.get()+1)
        cantjuegos.set(cantjuegos.get()+1)
    elif comando == "Divi":
        if resultado == divi():
            cantbuenos.set(cantbuenos.get()+1)
        else:
            cantmalos.set(cantmalos.get()+1)
        cantjuegos.set(cantjuegos.get()+1)

def multi():
    if int(n1.get()) !=0 and int(n2.get()) !=0:
        result = int(n1.get())* int(n2.get())
        return result
def divi():
    if int(n1.get()) !=0 and int(n2.get()) !=0:
        result = int(n1.get())/ int(n2.get())
        return result
def suma():
   result = int(n1.get())+ int(n2.get())
   return result
def restar():
    result = int(n1.get())- int(n2.get())
    return result
def go():
    global comando
    retornar(comando)
def nuevonum():
    global n1,n2, dif
    if dif == "Facil":
        n1.set(random.randint(0,10))
        n2.set( random.randint(0,10))
    elif dif == "Medio":
        n1.set(random.randint(0,100))
        n2.set( random.randint(0,100))
    elif dif == "Dificil":
        n1.set(random.randint(0,1000))
        n2.set( random.randint(0,1000))

def setdificultad():
    global dif
    if dificultad.get() == 1:
        dif = "Facil"
        resetearcontadores()
        return dif
    elif dificultad.get() == 2:
        dif = "Medio"
        resetearcontadores()
        return dif
    elif dificultad.get() == 3:
        dif = "Dificil"
        resetearcontadores()
        return dif
def resetearcontadores():
    global cantbuenos,cantjuegos,cantmalos
    cantmalos.set(0)
    cantbuenos.set(0)
    cantjuegos.set(0)
    n1.set(0)
    n2.set(0)
    valor.set(0)

ventana = tk.Tk()
ventana.title("Juego Matematico ")


operacion = tk.IntVar()
n1 = tk.IntVar(value=0)
lbl1 = tk.Label(ventana,text="Numero 1").grid()
entr1 = tk.Entry(ventana,textvariable=n1,state="readonly").grid()

n2= tk.IntVar(value=0)
lbl2 = tk.Label(ventana,text="Numero 2").grid()
entry2 = tk.Entry(ventana,textvariable=n2,state="readonly").grid()

nuevo = tk.Button(ventana,text="Nuevo Numero",command=nuevonum).grid()

lblo = tk.Label(ventana,text="Operaciones").grid(column=1, row=0)
sumar = tk.Radiobutton(ventana,text="Sumar",command=calcular,variable=operacion,value=1)
resta = tk.Radiobutton(ventana,text="Restar",command=calcular,variable=operacion,value=2)
multiplicar = tk.Radiobutton(ventana,text="Multiplicacion",command=calcular,variable=operacion,value=3)
division = tk.Radiobutton(ventana,text="Dividir",command=calcular,variable=operacion,value=4)

sumar.grid(column=1, row=1)
resta.grid(column=1, row=2)
multiplicar.grid(column=1, row=3)
division.grid(column=1, row=4)

cantjuegos = tk.IntVar(0)
juegos = tk.Label(ventana,text=f"Juegos: ")
juegos.grid(column=2,row=1)
numjuegos = tk.Label(ventana,textvariable=cantjuegos)
numjuegos.grid(column=3,row=1,padx=20)

cantbuenos = tk.IntVar()
buenos = tk.Label(ventana,text="Buenos: ")
buenos.grid(column=2,row=2)
numbuenos = tk.Label(ventana,textvariable=cantbuenos)
numbuenos.grid(column=3,row=2,padx=20)

cantmalos = tk.IntVar()
malos = tk.Label(ventana,text="Malos: ")
malos.grid(column=2,row=3)
nummalos = tk.Label(ventana,textvariable=cantmalos)
nummalos.grid(column=3,row=3,padx=20)


dificultad = tk.IntVar()
lbld = tk.Label(ventana,text="Dificultad")
lbld.grid(column=2,row=5)
facil = tk.Radiobutton(ventana,text="Facil",command=setdificultad,variable=dificultad,value=1)
facil.grid(column=2,row=6)
medio = tk.Radiobutton(ventana,text="Medio",command=setdificultad,variable=dificultad,value=2)
medio.grid(column=2,row=7)
dificil = tk.Radiobutton(ventana,text="Dificil",command=setdificultad,variable=dificultad,value=3)
dificil.grid(column=2,row=8)

valor = tk.IntVar(value=0)
lbl3 = tk.Label(ventana,text="Resultado").grid()
entry3 = tk.Entry(ventana,textvariable=valor).grid()


btn = tk.Button(ventana,text="Resultado",command=go).grid()
ventana.mainloop()