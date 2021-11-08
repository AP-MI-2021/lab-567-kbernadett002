from Domain.rezervare import getClasa, getCheckin, getPret, getId
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitate import trecereClasaSuperioara, ieftinireRezervare, ordonareDescrescator, sumaDupaNume, \
    pretMaximPeClase


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


def testOrdonareDescrescator():
    lista = []
    lista = adaugaRezervare("1", "Bernadett", "economy", 200, "DA", lista)
    lista = adaugaRezervare("2", "Costel", "economy plus", 300, "NU", lista)
    lista = adaugaRezervare("3", "Vivien", "business", 500, "DA", lista)

    rezultat = ordonareDescrescator(lista)

    assert getId(rezultat[0]) == "3"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "1"


def testSumaDupaNume():
    lista = []
    lista = adaugaRezervare("1", "Bernadett", "economy", 200, "DA", lista)
    lista = adaugaRezervare("2", "Costel", "economy plus", 300, "NU", lista)
    lista = adaugaRezervare("3", "Bernadett", "business", 500, "DA", lista)

    rezultat = sumaDupaNume(lista)

    assert len(rezultat) == 2
    assert rezultat["Bernadett"] == 700
    assert rezultat["Costel"] == 300


def testPretMaximPeClase():
    lista = []
    lista = adaugaRezervare("1", "Bernadett", "economy", 200, "DA", lista)
    lista = adaugaRezervare("2", "Costel", "economy plus", 300, "NU", lista)
    lista = adaugaRezervare("3", "Ana", "economy", 500, "DA", lista)

    rezultat = pretMaximPeClase(lista)

    assert rezultat[0] == 200
    assert rezultat[1] == 300
