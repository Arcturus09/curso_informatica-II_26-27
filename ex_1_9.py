def ex_1_9():
    dias=("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
    numero=int(input("Introduce un número del 1 al 7: "))
    if 1 <= numero <= 7:
        print("El día correspondiente es: ", dias[numero - 1])
    else:
        print("Error: el número debe estar entre 1 y 7.")

ex_1_9()
