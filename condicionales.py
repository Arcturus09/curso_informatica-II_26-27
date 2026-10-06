def condicionales():
    #07:00-12:00 -> Buenos días
    #12:00-20:00 -> Buenos tardes
    #20:00-07:00 -> Buenas noches
    #if(x>3):
        #rama del si
      #else:
        #rama del no

    while():
    tiempo=input("Dime qué hora es (hh:mm): ")
    hora=int(tiempo[0:2])
    if(hora<=7):
        print("Buenas noches")
    else:
        if(hora<=12):
            print("Buenos días")
        else:
            if(hora<=20):
                print("Buenas tardes")
            else:
                print("Buenas noches")

condicionales()
