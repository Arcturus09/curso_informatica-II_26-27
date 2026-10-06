def tabla_while():
    n_tabla=int(input("¿Qué tabla quieres que escriba (1-10)? "))
    print("*************************************")
    print("*            Tabla del "+str(n_tabla)+"            *")
    print("*************************************")
    cont=0
    while(cont<11):
        print(str(n_tabla)+" X "+str(cont)+" = "+str(n_tabla*cont))
        cont+=1 #es lo mismo que cont=cont+1

tabla_while()
