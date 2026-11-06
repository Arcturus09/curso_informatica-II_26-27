def ex_1_10():
    capitales={"España": "Madrid","Francia": "París","Italia": "Roma","Alemania": "Berlín"}
    pais=input("Introduce un país (recuerda usar mayúsculas): ")

    if pais in capitales:
        print("La capital de", pais, "es", capitales[pais])
    else:
        print("Error: el país no está en el diccionario.")

ex_1_10()
