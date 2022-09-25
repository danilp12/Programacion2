
import tkinter as tk
#   Variables Globales
paso = 0
#   Funciones
def mostrarmsj():
    global valorResta,valorSuma,valorFinal,op,resta,suma
    if paso == 0:
        nuevomarco()
        msj.set("Pensa un numero de dos cifras que no sean iguales..")
        btnsig = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
    elif paso == 1:
        nuevomarco()
        msj.set("Ahora invierte las cifras del numero")
        btnatras = tk.Button(frame,text="Atras",command=back).pack(side="left")
        btnsig = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
    elif paso == 2:
        nuevomarco()
        msj.set("El numero invertido es mayor que el numero pensado?")
        si = tk.Radiobutton(frame,text="Si",variable=op,value=1).pack()
        no = tk.Radiobutton(frame,text="No",variable=op,value=2).pack()
        btnatras = tk.Button(frame,text="Atras",command=back).pack(side="left")
        btnsig = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
        return op
    elif paso == 3:
        nuevomarco()
        resta = tk.Entry(frame,width=5)
        btnatras = tk.Button(frame,text="Atras",command=back).pack(side="left")
        if op.get() == 1:
            msj.set("Ahora resta el numero invertido menos el numero pensado")
            resta.pack()
            ok = tk.Button(frame,text="Cargar",command=asignarresta).pack()
        if op.get() == 2:
            msj.set("Ahora resta el numero pensado menos el numero invertido")
            resta.pack()
            ok = tk.Button(frame,text="Cargar",command=asignarresta).pack()
        return resta
    elif paso == 4:
        nuevomarco()
        btnatras = tk.Button(frame,text="Atras",command=back).pack(side="left")
        msj.set("ahora suma las dos cifras del numero pensado al principio")
        suma = tk.Entry(frame,width=5)
        suma.pack()
        ok = tk.Button(frame,text="Cargar",command=asignarsuma).pack()
        return suma
    elif paso == 5:
        nuevomarco()
        calcular()
        msj.set(f"El numero que pensaste es: ")
        lll = tk.Label(frame,text=f"{valorFinal.get()}",font="Helvetica").pack()
def nuevomarco():
    global frame
    frame.pack_forget()
    frame = tk.LabelFrame(ventana,text="Adivinanza de numeros")
    frame.pack(fill="both",expand="yes")
    lblmsj = tk.Label(frame,textvariable=msj).pack()
def asignarresta():
    global valorResta,resta
    valorResta.set(resta.get())
    next()
def asignarsuma():
    global valorSuma,suma
    valorSuma.set(suma.get())
    next()
def calcular():
    global op, valorFinal
    k = valorResta.get() /9
    a=int(( valorSuma.get() + k) / 2)
    b =int ((valorSuma.get() - k) / 2)
    if op.get() == 1:
        valor = str(b)+str(a)
        valorFinal.set(int(valor))
        return valorFinal
    elif op.get() == 2:
        valor = str(a)+str(b)
        valorFinal.set(int(valor))
        return valorFinal
def next():
    global paso
    paso += 1
    mostrarmsj()
    return paso
def back():
    global paso
    paso -= 1
    mostrarmsj()
    return paso
#   Ventana Principal
ventana = tk.Tk()
ventana.title("Juego Matematico - Adivinar Numero")
ventana.configure(bd=5,bg="#e4844a",padx=20,pady=20)
ventana.geometry("400x180")
op = tk.IntVar()
valorResta = tk.IntVar()
valorSuma = tk.IntVar()
valorFinal = tk.IntVar()

#   Mensaje
msj = tk.StringVar()
frame = tk.LabelFrame(ventana,text="Adivinanza de numeros")
frame.pack(fill="both",expand="yes")
lblmsj = tk.Label(frame,textvariable=msj)
lblmsj.pack()
mostrarmsj()
#   Boton Siguiente


ventana.mainloop()