import tkinter as tk
import random
def generar():
    n1 = int(entr1.get())
    n2 = int(entr2.get())
    if n2 > n1:
        n3 = random.randint(n1,n2)
        result.set(n3)
    else:
        n3 = 0
        result.set(n3)
        popup()

def popup():
    pop = tk.Toplevel()
    pop.geometry("300x50")
    tk.Label(pop,text="El numero 1 debe ser mas grande que el numero 2").grid()
    tk.Button(pop,text="Ok",command=pop.destroy).grid()

ventana = tk.Tk()
ventana.title("Generador de numeros ")
result = tk.IntVar()
lbl1 = tk.Label(ventana,text="Ingresar numero 1").grid()
entr1 = tk.Spinbox(ventana,from_=0,to=100)
entr1.grid()

lbl2 = tk.Label(ventana,text="Ingresar numero 2").grid()
entr2 = tk.Spinbox(ventana,from_=0,to=100)
entr2.grid()

lbl3 = tk.Label(ventana,text="Numeero Generado").grid()
entr3 = tk.Entry(ventana,state="readonly",textvariable=result)
entr3.grid()


#   Botones
btn = tk.Button(ventana,text="Generar",command=generar).grid()
ventana.mainloop()