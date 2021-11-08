from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergereRezervare, modificareRezervare
from Logic.functionalitate import trecereClasaSuperioara, ieftinireRezervare, pretMaximPeClase, ordonareDescrescator, \
    sumaDupaNume


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trecere la o clasa superioara")
    print("5. Ieftinire rezervare")
    print("6. Pret maxim pentru fiecare clasa")
    print("7. Ordonarea rezervărilor descrescător după preț.")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare rezervare")
    print("x. Iesire")


def uiAdaugareRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Alegeti clasa : economy/ economy plus/ business : ")
        pret = float(input("Dati pretul : "))
        checkin = input("Alegeti daca checkin-ul este facut : DA / NU : ")

        rezolvare = adaugaRezervare(id, nume, clasa, pret, checkin, lista)

        undoList.append(lista)
        redoList.clear()

        return rezolvare
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de sters: ")

        rezolvare = stergereRezervare(id, lista)

        undoList.append(lista)
        redoList.clear()

        return rezolvare
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificareRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii care trebuie modificata: ")
        nume = input("Dati noul nume: ")
        clasa = input("Alegeti noua clasa : economy/ economy plus/ business : ")
        pret = float(input("Dati noul pret : "))
        checkin = input("Alegeti daca checkin-ul este facut : DA / NU : ")

        rezolvare = modificareRezervare(id, nume, clasa, pret, checkin, lista)

        undoList.append(lista)
        redoList.clear()

        return rezolvare
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ShowAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiTrecereClasaSuperioara(lista, undoList, redoList):
    try:
        numeCitit = str(input("Dati un nume pentru a modifica clasa la rezervarea acestuia: "))

        rezolvare = trecereClasaSuperioara(numeCitit, lista)

        undoList.append(lista)
        redoList.clear()

        return rezolvare
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiIeftinireRezervare(lista, undoList, redoList):
    try:
        procentCitit = int(input("Dati procentul cu care se va ieftini rezervarea: "))

        rezolvare = ieftinireRezervare(procentCitit, lista)

        undoList.append(lista)
        redoList.clear()

        return rezolvare
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiPretMaximPeClase(lista):
    rez = pretMaximPeClase(lista)
    print("Pret maxim pe clase: ")
    print("Clasa economy: {} ; Clasa economy plus: {} ; Clasa business: {}".format(rez[0], rez[1], rez[2]))


def uiSumaDupaNume(lista):
    rezultat = sumaDupaNume(lista)
    for nume in rezultat:
        print("Persoana cu numele {}, are rezervari in valoare de : {} lei.".format(nume, rezultat[nume]))


def uiOrdonareDescrescator(lista, undoList, redoList):
    rezolvare = ordonareDescrescator(lista)

    undoList.append(lista)
    redoList.clear()

    return rezolvare


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareRezervare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergereRezervare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificareRezervare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiTrecereClasaSuperioara(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiIeftinireRezervare(lista, undoList, redoList)
        elif optiune == "6":
            uiPretMaximPeClase(lista)
        elif optiune == "7":
            lista = uiOrdonareDescrescator(lista, undoList, redoList)
        elif optiune == "8":
            uiSumaDupaNume(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            ShowAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune grestita!Reincercati!")
