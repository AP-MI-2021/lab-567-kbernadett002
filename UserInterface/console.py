from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergereRezervare, modificareRezervare


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("a. Afisare rezervare")
    print("x. Iesire")


def uiAdaugareRezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Alegeti clasa : economy/ economy plus/ business : ")
    pret = float(input("Dati pretul : "))
    checkin = input("Alegeti daca checkin-ul este facut : DA / NU : ")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def uiStergereRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return stergereRezervare(id, lista)


def uiModificareRezervare(lista):
    id = input("Dati id-ul rezervarii care trebuie modificata: ")
    nume = input("Dati noul nume: ")
    clasa = input("Alegeti noua clasa : economy/ economy plus/ business : ")
    pret = float(input("Dati noul pret : "))
    checkin = input("Alegeti daca checkin-ul este facut : DA / NU : ")
    return modificareRezervare(id, nume, clasa, pret, checkin, lista)


def ShowAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareRezervare(lista)
        elif optiune == "2":
            lista = uiStergereRezervare(lista)
        elif optiune == "3":
            lista = uiModificareRezervare(lista)
        elif optiune == "a":
            ShowAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune grestita!Reincercati!")



