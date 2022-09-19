import tkinter as tk

def multi():
    result = int(n1.get())* int(n2.get())
    valor.set(result)
def divi():
    result = int(n1.get())/ int(n2.get())
    valor.set(result)
def porcent():
    result = int(n1.get())% int(n2.get())
    valor.set(result)
def suma():
   result = int(n1.get())+ int(n2.get())
   valor.set(result)
def restar():
    result = int(n1.get())- int(n2.get())
    valor.set(result)
def reset():
    valor.set(0)
    n1.set(0)
    n2.set(0)
ventana = tk.Tk()
ventana.title("calculadora ")
n1 = tk.IntVar(value=0)
lbl1 = tk.Label(ventana,text="Numero 1").grid()
entr1 = tk.Entry(ventana,textvariable=n1).grid()

n2= tk.IntVar(value=0)
lbl2 = tk.Label(ventana,text="Numero 2").grid()
entry2 = tk.Entry(ventana,textvariable=n2).grid()

valor = tk.IntVar(value=0)
lbl3 = tk.Label(ventana,text="Resultado").grid()
entry3 = tk.Entry(ventana,textvariable=valor,state="readonly").grid()

#   Botones

btn1 = tk.Button(ventana,text="+",command=suma).grid()
btn2 = tk.Button(ventana,text="-",command=restar).grid()
btn3 = tk.Button(ventana,text="%",command=porcent).grid()
btn4 = tk.Button(ventana,text="*",command=multi).grid()
btn5 = tk.Button(ventana,text="/",command=divi).grid()
btn6 = tk.Button(ventana,text="Clear",command=reset).grid()
ventana.mainloop()