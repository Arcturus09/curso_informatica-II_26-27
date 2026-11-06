def ex_1_7():
    lista_notas=[4.5, 7, 3, 9.5, 6, 8, 5]
    print("Nota máxima: ", max(lista_notas))
    print("Nota mínima: ", min(lista_notas))
    print("Media: ", sum(lista_notas)/7)

    aprobados=0
    for nota in lista_notas:
        if nota>=5:
            print("Aprobado: "+str(nota))
        else:
            print("Suspendido: "+str(nota))

ex_1_7()
