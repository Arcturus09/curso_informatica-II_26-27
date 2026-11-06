def ex_1_3():
    nota=float(input("Dime tu nota (0 a 10): "))
    if(nota<5):
        print("Suspenso")
    else:
        if(nota<7):
            print("Bien")
        else:
            if(nota<9):
                print("Notable")
            else:
                if(nota<=10):
                    print("Sobresaliente")

ex_1_3()
