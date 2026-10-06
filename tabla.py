def tabla():
    n_tabla=int(input("¿Qué tabla quieres que escriba (1-10)? "))
    print("*************************************")
    print("*            Tabla del "+str(n_tabla)+"            *")
    print("*************************************")
    for cont in range (0,11):
        print(str(n_tabla)+" X "+str(cont)+" = "+str(n_tabla*cont))

tabla()
