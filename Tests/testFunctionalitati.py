from Domain.rezervare import getClasa, getCheckin, getPret
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitate import trecereClasaSuperioara, ieftinireRezervare


def testTrecereClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "Bernadett", "economy", 200, "DA", lista)
    lista = adaugaRezervare("2", "Costel", "economy plus", 300, "NU", lista)
    lista = adaugaRezervare("3", "Vivien", "business", 500, "DA", lista)

    lista = trecereClasaSuperioara("Bernadett", lista)

    assert getClasa(getById("1", lista)) == "economy plus"
    assert getClasa(getById("2", lista)) == "economy plus"
    assert getClasa(getById("3", lista)) == "business"


def testIeftinireRezervare():
    lista = []
    lista = adaugaRezervare("1", "Bernadett", "economy", 200, "DA", lista)
    lista = adaugaRezervare("2", "Costel", "economy plus", 300, "NU", lista)
    lista = adaugaRezervare("3", "Vivien", "business", 500, "DA", lista)

    lista = ieftinireRezervare(15, lista)

    assert getCheckin(getById("1", lista)) == "DA"
    assert getPret(getById("1", lista)) == 170
    assert getCheckin(getById("3", lista)) == "NU"
