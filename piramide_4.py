def piramide_4():
    #leer el número de pisos en la pirámide
    n_pisos=int(input("Introduce el número de pisos: "))
    #Hacemos un bucle para construir la pirámide piso a piso
    for fila in range(1,n_pisos+1):
        #Cada piso tiene un número de huecos + un número de asteriscos
        #Construimos una cadena concatenando el número huecos con el número de asteriscos
        cadena=(n_pisos-fila)*" "+(2*fila-1)*"*"
        #Mostramos la cadena por pantalla
        print(cadena,end="")
        #Cambiamos de línea
        print("")
        #Repetimos hasta el úlimo piso


piramide_4()
