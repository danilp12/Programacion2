
import tkinter as tk
#   Variables Globales
paso = -1
ffont = ("Lucida Console",13)
fontentry = ("Lucida Console",28)
fontboton = ("Helvetica",13)
#   Funciones
def mostrarmsj():
    global valorResta,valorSuma,valorFinal,op,resta,suma
    if paso == -1:
        global lang
        nuevomarco()
        msj.set("Elija el lenguaje")
        eng = tk.Radiobutton(frame,text="English",variable=lang,value=1,font=ffont,bg="#8b9e9b").pack()
        esp = tk.Radiobutton(frame,text="Español",variable=lang,value=2,font=ffont,bg="#8b9e9b").pack()
        btnsig = tk.Button(frame,text="Siguiente/Next",command=next,bg="#8b9e9b",font=fontboton).pack(side="right")
        return lang
    elif paso == 0 and lang.get() == 2:
        nuevomarco()
        msj.set("Pensa un numero de dos cifras que no sean iguales..")
        btnatras = tk.Button(frame,text="Atras",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        btnsig = tk.Button(frame,text="Siguiente",command=next,bg="#8b9e9b",font=fontboton).pack(side="right")
    elif paso == 0 and lang.get() == 1:
        nuevomarco()
        msj.set("Think of a two-digit number that is not the same..")
        btnatras = tk.Button(frame,text="Back",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        btnsig = tk.Button(frame,text="Next",command=next,bg="#8b9e9b",font=fontboton).pack(side="right")
    elif paso == 1 and lang.get() == 2:
        nuevomarco()
        msj.set("Ahora invierte las cifras del numero")
        btnatras = tk.Button(frame,text="Atras",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        btnsig = tk.Button(frame,text="Siguiente",command=next,bg="#8b9e9b",font=fontboton).pack(side="right")
    elif paso == 1 and lang.get() == 1:
        nuevomarco()
        msj.set("Now reverse the digits of the number")
        btnatras = tk.Button(frame,text="Back",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        btnsig = tk.Button(frame,text="Next",command=next,bg="#8b9e9b",font=fontboton).pack(side="right")
    elif paso == 2 and lang.get() == 2:
        nuevomarco()
        msj.set("El numero invertido es mayor que el numero pensado?")
        si = tk.Radiobutton(frame,text="Si",variable=op,value=1,bg="#8b9e9b",font=ffont).pack()
        no = tk.Radiobutton(frame,text="No",variable=op,value=2,bg="#8b9e9b",font=ffont).pack()
        btnatras = tk.Button(frame,text="Atras",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        btnsig = tk.Button(frame,text="Siguiente",command=next,bg="#8b9e9b",font=fontboton).pack(side="right")
        return op
    elif paso == 2 and lang.get() == 1:
        nuevomarco()
        msj.set("Is the inverted number greater than the intended number?")
        si = tk.Radiobutton(frame,text="Yes",variable=op,value=1,bg="#8b9e9b",font=ffont).pack()
        no = tk.Radiobutton(frame,text="No",variable=op,value=2,bg="#8b9e9b",font=ffont).pack()
        btnatras = tk.Button(frame,text="Back",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        btnsig = tk.Button(frame,text="Next",command=next,bg="#8b9e9b",font=fontboton).pack(side="right")
        return op
    elif paso == 3 and lang.get() == 2:
        nuevomarco()
        resta = tk.Entry(frame,width=3,font=fontentry)
        
        if op.get() == 1:
            msj.set("Ahora resta el numero invertido menos el numero pensado")
            resta.pack(fill = tk.Y)
            ok = tk.Button(frame,text="Cargar",command=asignarresta,bg="#8b9e9b",font=fontboton).pack(side="right")
        if op.get() == 2:
            msj.set("Ahora resta el numero pensado menos el numero invertido")
            resta.pack(fill = tk.Y)
            ok = tk.Button(frame,text="Cargar",command=asignarresta,bg="#8b9e9b",font=fontboton).pack(side="right")
        btnatras = tk.Button(frame,text="Atras",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        return resta
    elif paso == 3 and lang.get() == 1:
        nuevomarco()
        resta = tk.Entry(frame,width=3,font=fontentry)
        
        if op.get() == 1:
            msj.set("Now subtract the inverted number minus the thought number")
            resta.pack(fill = tk.Y)
            ok = tk.Button(frame,text="Load",command=asignarresta,bg="#8b9e9b",font=fontboton).pack(side="right")
        if op.get() == 2:
            msj.set("Now subtract the number thought minus the number inverted")
            resta.pack(fill = tk.Y)
            ok = tk.Button(frame,text="Load",command=asignarresta,bg="#8b9e9b",font=fontboton).pack(side="right")
        btnatras = tk.Button(frame,text="Back",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        return resta
    elif paso == 4 and lang.get() == 2:
        nuevomarco()
        
        msj.set("ahora suma las dos cifras del numero pensado al principio")
        suma = tk.Entry(frame,width=3,font=fontentry)
        suma.pack(fill = tk.Y)
        btnatras = tk.Button(frame,text="Atras",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        ok = tk.Button(frame,text="Cargar",command=asignarsuma,bg="#8b9e9b",font=fontboton).pack(side="right")
        return suma
    elif paso == 4 and lang.get() == 1:
        nuevomarco()
        
        msj.set("now sum the two digits of the number you thought at the beginning")
        suma = tk.Entry(frame,width=3,font=fontentry)
        suma.pack(fill = tk.Y)
        btnatras = tk.Button(frame,text="Back",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        ok = tk.Button(frame,text="Load",command=asignarsuma,bg="#8b9e9b",font=fontboton).pack(side="right")
        return suma
    elif paso == 5 and lang.get() == 2:
        nuevomarco()
        calcular()
        msj.set(f"El numero que pensaste es: ")
        lll = tk.Label(frame,text=f"{valorFinal.get()}",bg="#8b9e9b",font=("Helvetica",50)).pack()
        btnatras = tk.Button(frame,text="Atras",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        btnsig = tk.Button(frame,text="Reiniciar",command=restart,bg="#8b9e9b",font=fontboton).pack(side="right")
    elif paso == 5 and lang.get() == 1:
        nuevomarco()
        calcular()
        msj.set(f"The number you thought is: ")
        lll = tk.Label(frame,text=f"{valorFinal.get()}",bg="#8b9e9b",font=("Helvetica",50)).pack()
        btnatras = tk.Button(frame,text="Back",command=back,bg="#8b9e9b",font=fontboton).pack(side="left")
        btnsig = tk.Button(frame,text="Restart",command=restart,bg="#8b9e9b",font=fontboton).pack(side="right")
def nuevomarco():
    global frame
    frame.pack_forget()
    if lang.get() == 2:
        frame = tk.LabelFrame(ventana,text="Adivinanza de numeros",font=ffont,bg="#a65d53")
        frame.pack(fill="both",expand="yes")
        lblmsj = tk.Label(frame,textvariable=msj,font=ffont,bg="#a65d53").pack()
    elif lang.get() == 1:
        frame = tk.LabelFrame(ventana,text="Number riddle",font=ffont,bg="#a65d53")
        frame.pack(fill="both",expand="yes")
        lblmsj = tk.Label(frame,textvariable=msj,font=ffont,bg="#a65d53").pack()
def restart():
    global paso
    paso = -1
    mostrarmsj()
    return paso
def asignarresta():
    global valorResta,resta
    if resta.get() != "0" and resta.get() != "" and resta.get().isnumeric():
        valorResta.set(resta.get())
        next()
def asignarsuma():
    global valorSuma,suma
    if suma.get() != "0" and suma.get() !="" and suma.get().isnumeric():
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
ventana.configure(relief="sunken",bd=5,bg="#63072c",padx=20,pady=20)
ventana.geometry("700x220")
op = tk.IntVar()
lang = tk.IntVar()
lang.set(2)
valorResta = tk.IntVar()
valorSuma = tk.IntVar()
valorFinal = tk.IntVar()

#   Mensaje
msj = tk.StringVar()
frame = tk.LabelFrame(ventana,text="Adivinanza de numeros",font=ffont,bg="#a65d53")
frame.pack(fill="both",expand="yes")
lblmsj = tk.Label(frame,textvariable=msj,font=ffont)
lblmsj.pack()
mostrarmsj()
#   Boton Siguiente


ventana.mainloop()