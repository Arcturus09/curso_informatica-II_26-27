def ex_1_6():
    numero=int(input("Introduce un múmero (0 para terminar): "))
    contador=0
    suma=0
    while numero !=0:
        contador +=1
        suma +=numero
        numero=int(input("Introduce otro numero (0 para terminar)"))

    print("Cantidad de números: ", contador)
    print("Suma total: ", suma)

ex_1_6()
