def ex_1_5():
    n_tabla=int(input("¿Qué tabla quieres que escriba (1-10)? "))
    print("*************************************")
    print("*            Tabla del "+str(n_tabla)+"            *")
    print("*************************************")
    for number in range(1, 11):
        print(str(n_tabla)+" X "+str(number)+" = "+str(n_tabla*number))

ex_1_5()
