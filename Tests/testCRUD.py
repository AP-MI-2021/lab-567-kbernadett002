from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, getById, stergereRezervare, modificareRezervare


def testAdaugaRezervare():
    lista=[]
    lista=adaugaRezervare("1", "Kiss Bernadett", "economy", 200, "DA", lista)

    assert getId(getById("1",lista)) == "1"
    assert getNume(lista[0]) == "Kiss Bernadett"
    assert getClasa(lista[0]) == "economy"
    assert getPret(lista[0]) == 200
    assert getCheckin(lista[0]) == "DA"



def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("1", "Kiss Bernadett", "economy", 200, "DA", lista)
    lista = adaugaRezervare("2", "Ana Maria", "business", 200, "DA", lista)

    lista = stergereRezervare("1",lista)

    assert (len(lista) == 1)
    assert getById("1", lista) is None
    assert getById("2", lista) is not None


def testModificaRezervare():
    lista=[]
    lista = adaugaRezervare("1", "Kiss Bernadett", "economy", 200, "DA", lista)
    lista = adaugaRezervare("2", "Ana Maria", "business", 200, "DA", lista)

    lista = modificareRezervare("2", "Eduard", "business", 250, "DA", lista)

    assert getNume(lista[1]) == "Eduard"
    assert getClasa(lista[1]) == "business"
    assert getPret(lista[1]) == 250
    assert getCheckin(lista[1]) == "DA"



