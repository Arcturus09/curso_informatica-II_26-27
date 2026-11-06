def piramide():
    n_pisos=int(input("¿Cuántos pisos quieres? "))
    cadena=""
    for cont in range(1,n_pisos+1):
        cadena=cadena+"*"
        print(cadena)

piramide()
