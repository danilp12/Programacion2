
import tkinter as tk
#   Variables Globales
paso = -1
#   Funciones
def mostrarmsj():
    global valorResta,valorSuma,valorFinal,op,resta,suma
    if paso == -1:
        global lang
        nuevomarco()
        msj.set("Elija el lenguaje")
        eng = tk.Radiobutton(frame,text="English",variable=lang,value=1).pack()
        esp = tk.Radiobutton(frame,text="Español",variable=lang,value=2).pack()
        btnsig = tk.Button(frame,text="Siguiente/Next",command=next).pack(side="right")
        return lang
    elif paso == 0 and lang.get() == 2:
        nuevomarco()
        msj.set("Pensa un numero de dos cifras que no sean iguales..")
        btnatras = tk.Button(frame,text="Atras",command=back).pack(side="left")
        btnsig = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
    elif paso == 0 and lang.get() == 1:
        nuevomarco()
        msj.set("Think of a two-digit number that is not the same..")
        btnatras = tk.Button(frame,text="Back",command=back).pack(side="left")
        btnsig = tk.Button(frame,text="Next",command=next).pack(side="right")
    elif paso == 1 and lang.get() == 2:
        nuevomarco()
        msj.set("Ahora invierte las cifras del numero")
        btnatras = tk.Button(frame,text="Atras",command=back).pack(side="left")
        btnsig = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
    elif paso == 1 and lang.get() == 1:
        nuevomarco()
        msj.set("Now reverse the digits of the number")
        btnatras = tk.Button(frame,text="Back",command=back).pack(side="left")
        btnsig = tk.Button(frame,text="Next",command=next).pack(side="right")
    elif paso == 2 and lang.get() == 2:
        nuevomarco()
        msj.set("El numero invertido es mayor que el numero pensado?")
        si = tk.Radiobutton(frame,text="Si",variable=op,value=1).pack()
        no = tk.Radiobutton(frame,text="No",variable=op,value=2).pack()
        btnatras = tk.Button(frame,text="Atras",command=back).pack(side="left")
        btnsig = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
        return op
    elif paso == 2 and lang.get() == 1:
        nuevomarco()
        msj.set("Is the inverted number greater than the intended number?")
        si = tk.Radiobutton(frame,text="Yes",variable=op,value=1).pack()
        no = tk.Radiobutton(frame,text="No",variable=op,value=2).pack()
        btnatras = tk.Button(frame,text="Back",command=back).pack(side="left")
        btnsig = tk.Button(frame,text="Next",command=next).pack(side="right")
        return op
    elif paso == 3 and lang.get() == 2:
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
    elif paso == 3 and lang.get() == 1:
        nuevomarco()
        resta = tk.Entry(frame,width=5)
        btnatras = tk.Button(frame,text="Back",command=back).pack(side="left")
        if op.get() == 1:
            msj.set("Now subtract the inverted number minus the thought number")
            resta.pack()
            ok = tk.Button(frame,text="Load",command=asignarresta).pack()
        if op.get() == 2:
            msj.set("Now subtract the number thought minus the number inverted")
            resta.pack()
            ok = tk.Button(frame,text="Load",command=asignarresta).pack()
        return resta
    elif paso == 4 and lang.get() == 2:
        nuevomarco()
        btnatras = tk.Button(frame,text="Atras",command=back).pack(side="left")
        msj.set("ahora suma las dos cifras del numero pensado al principio")
        suma = tk.Entry(frame,width=5)
        suma.pack()
        ok = tk.Button(frame,text="Cargar",command=asignarsuma).pack()
        return suma
    elif paso == 4 and lang.get() == 1:
        nuevomarco()
        btnatras = tk.Button(frame,text="Back",command=back).pack(side="left")
        msj.set("now add the two digits of the number you thought at the beginning")
        suma = tk.Entry(frame,width=5)
        suma.pack()
        ok = tk.Button(frame,text="Load",command=asignarsuma).pack()
        return suma
    elif paso == 5 and lang.get() == 2:
        nuevomarco()
        calcular()
        msj.set(f"El numero que pensaste es: ")
        lll = tk.Label(frame,text=f"{valorFinal.get()}",font="Helvetica").pack()
    elif paso == 5 and lang.get() == 1:
        nuevomarco()
        calcular()
        msj.set(f"The number you thought is: ")
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
lang = tk.IntVar()
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