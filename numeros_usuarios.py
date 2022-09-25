




# while True:
#     print("Pensa un numero de dos cifras que no sean iguales")
#     num = int(input("Cuando lo pienses, ingresalo: "))
#     num_inv =int (str(num)[1]+str(num)[0])
#     print(f"El numero invertido es:{num_inv} ")
#     if num_inv > num:
#         print(f"El numero invertido es mas grande que el que habias ingresado.")
#         n1 = num_inv - num
#     else:
#         print("El numero invertido es menor que el numero ingresado")
#         n1 = num - num_inv
#     n2 = int(str(num)[0]) + int(str(num)[1])
#     termino1 = n1 / 2
#     termino2 = (n2-2) /2
#     termino3 = (n2+2) /2
#     print(f"el numero que pensaste es el {int(termino2)}{int(termino3)}")
#     break


while True:
    print("Pensa un numero de dos cifras que no sean iguales..")
    input("Toca una tecla cuando lo tengas pensado")
    print("Ahora invierte las cifras del numero")
    input("Toca una tecla cuando estes listo")
    
    esmayor = int(input("El numero invertido es mayor que el numero pensado? -1- SI -2- NO: "))
    if esmayor == 1:
        print("Ahora resta el numero invertido menos el numero pensado")
    else: print("Ahora resta el numero pensado menos el numero invertido")
    resta = int(input("Ingresa el valor de la resta: ")   ) 
    print("ahora suma las dos cifras del numero pensado al principio")
    suma = int(input("Ingresa el valor de la suma: "))
    k = resta /9
    a=int(( suma + k) / 2)
    b =int ((suma - k) / 2)
    if esmayor == 1:
        print(f"El numero que pensaste es {b}{a}")
    else : print(f"El numero que pensaste es {a}{b}")