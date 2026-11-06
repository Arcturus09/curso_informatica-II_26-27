def ex_1_8():
    nombres = []
    for vuelta in range(0, 5):
        un_nombre = input("Introduce el nombre " + str(vuelta + 1) + ": ")
        nombres.append(un_nombre)

    print("\nNombres en orden inverso:")
    for vuelta in range(4, -1, -1):
        print(nombres[vuelta])

ex_1_8()
