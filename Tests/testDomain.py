from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin


def testRezervare():
    rezervare = creeazaRezervare("1", "Kiss Bernadett", "economy", 200, "DA")

    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "Kiss Bernadett"
    assert getClasa(rezervare) == "economy"
    assert getPret(rezervare) == 200
    assert getCheckin(rezervare) == "DA"


