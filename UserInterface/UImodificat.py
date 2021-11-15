from Domain.rezervare import toString
from Logic.CRUD import modificareRezervare, adaugaRezervare, stergereRezervare


def print_comenzi():
    print("help == Afisare utilizare meniu")
    print("add ==  Adaugare rezervare")
    print("delete ==  Stergere rezervare")
    print("update == Modificare rezervare")
    print("showAll == Afisare rezervare")
    print("stop ==  Iesire")


def adauga_rezervare(id, nume, clasa, pret, checkin, lista):
    try:
        return adaugaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def modificare_rezervare(id, nume, clasa, pret, checkin, lista):
    try:
        return modificareRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def stergere_rezervare(id, lista):
    try:
        return stergereRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def afisare_toate(lista):
    for rezervare in lista:
        print(toString(rezervare))


def meniu(lista):
    merge = True
    while merge is True:
        comenzi = input("Intorduceti comanda: ")
        comandaLista = comenzi.split(";")
        for c in comandaLista:
            comanda = c.split(",")
            if comanda[0] == "add":
                try:
                    lista = adauga_rezervare(comanda[1], comanda[2], comanda[3],
                                             float(comanda[4]), comanda[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif comanda[0] == "delete":
                try:
                    lista = stergere_rezervare(comanda[1], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif comanda[0] == "update":
                try:
                    lista = modificare_rezervare(comanda[1], comanda[2], comanda[3],
                                                 float(comanda[4]), comanda[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif comanda[0] == "showAll":
                afisare_toate(lista)
            elif comanda[0] == "help":
                print_comenzi()
            elif comanda[0] == "stop":
                merge = False
            else:
                print("Comanda gresita! Incercati din nou!")
