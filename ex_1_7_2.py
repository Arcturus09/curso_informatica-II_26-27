def ex_1_7_2():
    lista_notas=[4.5, 7, 3, 9.5, 6, 8, 5]
    maximo=lista_notas[0]
    minimo=lista_notas[0]
#    print("Nota máxima: ", max(lista_notas))
#    print("Nota mínima: ", min(lista_notas))
    print("Media: ", sum(lista_notas)/7)

    aprobados=0
    for nota in lista_notas:
        if (nota>maximo):
            maximo=nota
        if (nota<minimo):
            minimo=nota
        if (nota>=5):
            print("Aprobado: "+str(nota))
        else:
            print("Suspendido: "+str(nota))

    print("Nota máxima: "+str(maximo))
    print("Nota máxima: "+str(minimo))

ex_1_7_2()
