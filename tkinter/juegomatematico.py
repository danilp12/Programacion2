

import tkinter as tk
import random, time, os
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
    n1.set(0)
    n2.set(0)
    valor.set(0)
    bloqueodeoperacion()
    return temp
def nuevonum():
    global n1,n2, dif, inicio, temp
    temp = True
    inicio = time.time()
    temporizador()
    sortearoperacion()
    if dif == "Facil":
        n1.set(random.randint(0,10))
        n2.set( random.randint(0,10))
    elif dif == "Medio":
        n1.set(random.randint(0,100))
        n2.set( random.randint(0,100))
    elif dif == "Dificil":
        n1.set(random.randint(0,1000))
        n2.set( random.randint(0,1000))
    msjproblema()
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
def sortearoperacion():
    global operacion
    num = random.randint(1,4)
    operacion.set(num)
    if num == 1:
        sumar.configure(state="active")
    elif num == 2:
        resta.configure(state="active")
    elif num == 3:
        multiplicar.configure(state="active")
    elif num == 4:
        division.configure(state="active")
    calcular()
    return operacion
def bloqueodeoperacion():
    sumar.configure(state="disabled")
    resta.configure(state="disabled")
    multiplicar.configure(state="disabled")
    division.configure(state="disabled")
def msjproblema():
    global operacion, msj
    if operacion.get() == 1:
        op = " + "
    elif operacion.get() == 2:
        op = " - "
    elif operacion.get() == 3:
        op = " * "
    elif operacion.get() == 4:
        op = " / "
    msj.set(f"{n1.get()} {op} {n2.get()} = ") 
    return msj

#   Ventana Principal
ventana = tk.Tk()
ventana.title("Juego Matematico ")
ventana.configure(bd=5,bg="#e4844a",padx=20,pady=20)
msj = tk.StringVar()

#       Campo numero 1
n1 = tk.IntVar(value=0)
lbl1 = tk.Label(ventana,text="Numero 1",font="Helvetica",background="#ba1e4a").grid(column=0,row=0,padx=5,pady=5)
entr1 = tk.Entry(ventana,textvariable=n1,state="readonly",font="Helvetica",background="#e4844a",width=5).grid(column=0,row=1)
#       Campo numero 2
n2= tk.IntVar(value=0)
lbl2 = tk.Label(ventana,text="Numero 2",font="Helvetica",background="#ba1e4a").grid(column=0,row=2,padx=5,pady=5)
entry2 = tk.Entry(ventana,textvariable=n2,state="readonly",font="Helvetica",background="#e4844a",width=5).grid(column=0,row=3)
#       Boton de nuevo numero
nuevo = tk.Button(ventana,text="Nuevo Numero",command=nuevonum,font="Helvetica",background="#b68810",border=10).grid(column=0,row=4,padx=5,pady=5)
#       Operaciones
operacion = tk.IntVar()
lblo = tk.Label(ventana,text="Operaciones",font="Helvetica",background="#ba1e4a").grid(column=1, row=0,padx=5,pady=5)
sumar = tk.Radiobutton(ventana,text="Sumar",command=calcular,variable=operacion,value=1,background="#e4844a",state="disabled")
resta = tk.Radiobutton(ventana,text="Restar",command=calcular,variable=operacion,value=2,background="#e4844a",state="disabled")
multiplicar = tk.Radiobutton(ventana,text="Multiplicacion",command=calcular,variable=operacion,value=3,background="#e4844a",state="disabled")
division = tk.Radiobutton(ventana,text="Dividir",command=calcular,variable=operacion,value=4,background="#e4844a",state="disabled")
sumar.grid(column=1, row=1)
resta.grid(column=1, row=2)
multiplicar.grid(column=1, row=3)
division.grid(column=1, row=4)
#       Stat Juego
cantjuegos = tk.IntVar(0)
juegos = tk.Label(ventana,text=f"Juegos:",font="Helvetica",background="#e4844a",width=10)
juegos.grid(column=1,row=6)
numjuegos = tk.Label(ventana,textvariable=cantjuegos,font="Helvetica",background="#e4844a",width=5)
numjuegos.grid(column=2,row=6,padx=5)
#       Stat Ganados
cantbuenos = tk.IntVar()
buenos = tk.Label(ventana,text="Buenos:",font="Helvetica",background="#e4844a",width=10)
buenos.grid(column=1,row=7)
numbuenos = tk.Label(ventana,textvariable=cantbuenos,font="Helvetica",background="#e4844a",width=5)
numbuenos.grid(column=2,row=7,padx=5)
#       Stat Perdidos
cantmalos = tk.IntVar()
malos = tk.Label(ventana,text="Malos:",font="Helvetica",background="#e4844a",width=10)
malos.grid(column=1,row=8)
nummalos = tk.Label(ventana,textvariable=cantmalos,font="Helvetica",background="#e4844a",width=5)
nummalos.grid(column=2,row=8,padx=5)

#       Dificultad
dificultad = tk.IntVar()
lbld = tk.Label(ventana,text="Dificultad",font="Helvetica",background="#ba1e4a")
lbld.grid(column=3,row=0)
facil = tk.Radiobutton(ventana,text="Facil - Numeros del 0-10 - (60 Seg)",command=setdificultad,variable=dificultad,value=1,background="#e4844a")
facil.grid(column=3,row=1)
medio = tk.Radiobutton(ventana,text="Medio - Numeros del 0-100 -(45 Seg)",command=setdificultad,variable=dificultad,value=2,background="#e4844a")
medio.grid(column=3,row=2)
dificil = tk.Radiobutton(ventana,text="Dificil - Numeros del 0-1000 -(30 Seg)",command=setdificultad,variable=dificultad,value=3,background="#e4844a")
dificil.grid(column=3,row=3)
#       Tiempo
tiempo = tk.StringVar()
tempo = tk.Label(ventana,text="Tiempo",font="Helvetica",background="#ba1e4a").grid(column=0,row=6,padx=5,pady=5)
tiempolbl = tk.Label(ventana,textvariable=tiempo,font="Helvetica",background="#e8bf56").grid(column=0,row=7,padx=5,pady=5)
#       Resultado
valor = tk.IntVar(value=0)
lbl3 = tk.Label(ventana,text="Resultado",font="Helvetica",background="#ba1e4a").grid(column=0,row=8,padx=5,pady=5)
msnj = tk.Label(ventana,textvariable=msj,font="Helvetica").grid(column=0,row=9,padx=5,pady=5)
entry3 = tk.Entry(ventana,textvariable=valor,font="Helvetica",width=5).grid(column=0,row=10,padx=5,pady=5)

#       Imagen
imagen = tk.PhotoImage(file=os.getcwd()+"\\tkinter\imagen.png")
img = tk.Label(ventana,image=imagen,borderwidth=0)
img.grid(column=3,row=6,rowspan=3)
#       Boton Resultado
btn = tk.Button(ventana,text="Resultado",command=go,font="Helvetica",background="#b68810",border=10).grid(column=0,row=11, pady=20)
ventana.mainloop()