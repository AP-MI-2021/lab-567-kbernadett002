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
    ok = True
    while ok is True:
        comenzi = input("Intorduceti comanda: ")
        comandaLista = comenzi.split(";")
        optiune = comandaLista[0]
        for c in comandaLista[1:]:
            comanda = c.split(",")
            if optiune == "add":
                try:
                    lista = adauga_rezervare(comanda[0], comanda[1], comanda[2], float(comanda[3]), comanda[4], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif optiune == "delete":
                try:
                    lista = stergere_rezervare(comanda[0], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif optiune == "update":
                try:
                    e = modificare_rezervare(comanda[0], comanda[1], comanda[2], float(comanda[3]), comanda[4], lista)
                    lista = e
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif optiune == "showAll":
                afisare_toate(lista)
            elif optiune == "help":
                print_comenzi()
            elif optiune == "stop":
                ok = False
            else:
                print("Comanda gresita! Incercati din nou!")
