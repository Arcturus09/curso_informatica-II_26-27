def piramide_3():
    n_pisos=int(input("¿Cuántos pisos quieres? "))
    for fil in range(1,n_pisos+1):
        for col in range(1,fil+1):
            print("*",end="")
        print("")

piramide_3()
