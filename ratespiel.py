import random
durchgang = 0
aktiv = True
ratezahl = random.randint(0, 100)

while aktiv:
    durchgang = durchgang + 1
    print()
    print(durchgang)
    benutzereingabe = int(input("Bitte Zahl eingeben:"))

    if ratezahl == benutzereingabe:
        print("Gewonnen! Die geheime Zahl ist nicht mehr geheim.")
        aktiv = False
        break

    elif benutzereingabe > ratezahl:
        print("Deine Zahl ist zu groß")

    else:
        print("Deine Zahl ist zu klein")

    if durchgang == 7:
        print("Schade du hast verloren")
        print("Es war die Zahl" + str(ratezahl))
        aktiv = False
print("Spiel Ende")
