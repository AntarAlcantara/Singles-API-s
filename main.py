opc = 0
while opc != 5:
    print(" _________________________")
    print("|   1.-   Interpretes     |")
    print("|_________________________|")
    print("|   2.-     Albums        |")
    print("|_________________________|")
    print("|   3.-    Canciones      |")
    print("|_________________________|")
    print("|   4.-     Salir         |")
    print("|_________________________|")


    opc=int(input("Elige una opcion: "))
    if opc == 1:
      exec(open("Interprete.py").read())
    if opc == 2:
      exec(open("album.py").read())
    if opc ==3:
      exec(open("canciones.py").read())
    if opc ==4:
      print("Fin de la evaluacion")
