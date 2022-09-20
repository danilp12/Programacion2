

import tkinter as tk
import random, time
inicio = ""
dif = "Facil"
tiempojuego = 30
comando =""
temp = True
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
    else:
        result = 0
        return result
def divi():
    if int(n1.get()) !=0 and int(n2.get()) !=0:
        result = int(n1.get())/ int(n2.get())
        return result
    else:
        result = 0
        return result
def suma():
   result = int(n1.get())+ int(n2.get())
   return result
def restar():
    result = int(n1.get())- int(n2.get())
    return result
def go():
    global comando, temp
    retornar(comando)
    tiempo.set("--")
    temp = False
    return temp
def nuevonum():
    global n1,n2, dif, inicio, temp
    temp = True
    inicio = time.time()
    temporizador()
    if dif == "Facil":
        n1.set(random.randint(0,10))
        n2.set( random.randint(0,10))
    elif dif == "Medio":
        n1.set(random.randint(0,100))
        n2.set( random.randint(0,100))
    elif dif == "Dificil":
        n1.set(random.randint(0,1000))
        n2.set( random.randint(0,1000))
    return inicio

def setdificultad():
    global dif, tiempojuego
    if dificultad.get() == 1:
        dif = "Facil"
        tiempojuego = 60
        resetearcontadores()
        return dif,tiempojuego
    elif dificultad.get() == 2:
        dif = "Medio"
        tiempojuego = 45
        resetearcontadores()
        return dif, tiempojuego
    elif dificultad.get() == 3:
        dif = "Dificil"
        tiempojuego = 30
        resetearcontadores()
        return dif, tiempojuego
def resetearcontadores():
    global cantbuenos,cantjuegos,cantmalos, temp
    cantmalos.set(0)
    cantbuenos.set(0)
    cantjuegos.set(0)
    n1.set(0)
    n2.set(0)
    valor.set(0)
    temp = False

def temporizador():
    global inicio ,temp 
    if temp:
        now = time.time()
        actual =str (now-inicio)[0:3]
        
        if float(actual) == float(tiempojuego):
            tiempo.set("--")
            perdido()
            cantjuegos.set(cantjuegos.get()+1)
            cantmalos.set(cantmalos.get()+1)
        else:
            tiempo.set(actual + " Segundos")
            ventana.after(1000, temporizador)
    
    
def perdido():
    pop = tk.Toplevel()
    pop.geometry("180x80")
    pop.configure(bg="#e4844a",padx=20,pady=20)
    tk.Label(pop,text="Has perdido el turno",bg="#e4844a",font="Helvetica").grid()
    tk.Button(pop,text="Ok",command=pop.destroy,bg="#e4844a",font="Helvetica").grid()

ventana = tk.Tk()
ventana.title("Juego Matematico ")
ventana.configure(bd=5,bg="#e4844a",padx=20,pady=20)


operacion = tk.IntVar()
n1 = tk.IntVar(value=0)
lbl1 = tk.Label(ventana,text="Numero 1",font="Helvetica",background="#ba1e4a").grid(column=0,row=0,padx=5,pady=5)
entr1 = tk.Entry(ventana,textvariable=n1,state="readonly",font="Helvetica",background="#e4844a",width=5).grid(column=0,row=1)

n2= tk.IntVar(value=0)
lbl2 = tk.Label(ventana,text="Numero 2",font="Helvetica",background="#ba1e4a").grid(column=0,row=2,padx=5,pady=5)
entry2 = tk.Entry(ventana,textvariable=n2,state="readonly",font="Helvetica",background="#e4844a",width=5).grid(column=0,row=3)

nuevo = tk.Button(ventana,text="Nuevo Numero",command=nuevonum,font="Helvetica",background="#b68810",border=10).grid(column=0,row=4,padx=5,pady=5)

lblo = tk.Label(ventana,text="Operaciones",font="Helvetica",background="#ba1e4a").grid(column=1, row=0,padx=5,pady=5)
sumar = tk.Radiobutton(ventana,text="Sumar",command=calcular,variable=operacion,value=1,background="#e4844a")
resta = tk.Radiobutton(ventana,text="Restar",command=calcular,variable=operacion,value=2,background="#e4844a")
multiplicar = tk.Radiobutton(ventana,text="Multiplicacion",command=calcular,variable=operacion,value=3,background="#e4844a")
division = tk.Radiobutton(ventana,text="Dividir",command=calcular,variable=operacion,value=4,background="#e4844a")

sumar.grid(column=1, row=1)
resta.grid(column=1, row=2)
multiplicar.grid(column=1, row=3)
division.grid(column=1, row=4)

cantjuegos = tk.IntVar(0)
juegos = tk.Label(ventana,text=f"Juegos: ",font="Helvetica",background="#e4844a",width=10)
juegos.grid(column=1,row=6)
numjuegos = tk.Label(ventana,textvariable=cantjuegos,font="Helvetica",background="#e4844a",width=5)
numjuegos.grid(column=2,row=6,padx=5)

cantbuenos = tk.IntVar()
buenos = tk.Label(ventana,text="Buenos: ",font="Helvetica",background="#e4844a",width=10)
buenos.grid(column=1,row=7)
numbuenos = tk.Label(ventana,textvariable=cantbuenos,font="Helvetica",background="#e4844a",width=5)
numbuenos.grid(column=2,row=7,padx=5)

cantmalos = tk.IntVar()
malos = tk.Label(ventana,text="Malos: ",font="Helvetica",background="#e4844a",width=10)
malos.grid(column=1,row=8)
nummalos = tk.Label(ventana,textvariable=cantmalos,font="Helvetica",background="#e4844a",width=5)
nummalos.grid(column=2,row=8,padx=5)


dificultad = tk.IntVar()
lbld = tk.Label(ventana,text="Dificultad",font="Helvetica",background="#ba1e4a")
lbld.grid(column=3,row=0)
facil = tk.Radiobutton(ventana,text="Facil - Numeros del 0-10 - (60 Seg)",command=setdificultad,variable=dificultad,value=1,background="#e4844a")
facil.grid(column=3,row=1)
medio = tk.Radiobutton(ventana,text="Medio - Numeros del 0-100 -(45 Seg)",command=setdificultad,variable=dificultad,value=2,background="#e4844a")
medio.grid(column=3,row=2)
dificil = tk.Radiobutton(ventana,text="Dificil - Numeros del 0-1000 -(30 Seg)",command=setdificultad,variable=dificultad,value=3,background="#e4844a")
dificil.grid(column=3,row=3)

tiempo = tk.StringVar()
tempo = tk.Label(ventana,text="Tiempo",font="Helvetica",background="#ba1e4a").grid(column=0,row=6,padx=5,pady=5)
tiempolbl = tk.Label(ventana,textvariable=tiempo,font="Helvetica",background="#e8bf56").grid(column=0,row=7,padx=5,pady=5)

valor = tk.IntVar(value=0)
lbl3 = tk.Label(ventana,text="Resultado",font="Helvetica",background="#ba1e4a").grid(column=0,row=8,padx=5,pady=5)
entry3 = tk.Entry(ventana,textvariable=valor,font="Helvetica",width=5).grid(column=0,row=9,padx=5,pady=5)


btn = tk.Button(ventana,text="Resultado",command=go,font="Helvetica",background="#b68810",border=10).grid(column=0,row=10, pady=20)
ventana.mainloop()