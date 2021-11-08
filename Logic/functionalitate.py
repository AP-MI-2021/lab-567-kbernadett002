from Domain.rezervare import getNume, getClasa, creeazaRezervare, getId, getPret, getCheckin


def trecereClasaSuperioara(numeCitit, lista):
    """
    Trece toate rezervarile facute la un nume citit la o clasa superioara
    :param numeCitit: un string
    :param lista:o lista
    :return: o lista de rezervari
    """
    listaNoua = []
    for rezervare in lista:
        if getNume(rezervare) == numeCitit:
            tipClasa = getClasa(rezervare)
            if tipClasa == "economy":
                tipClasa = "economy plus"
                rezervareNoua1 = creeazaRezervare(
                    getId(rezervare),
                    getNume(rezervare),
                    tipClasa,
                    getPret(rezervare),
                    getCheckin(rezervare)
                )
                listaNoua.append(rezervareNoua1)
            elif tipClasa == "economy plus":
                tipClasa = "business"
                rezervareNoua2 = creeazaRezervare(
                    getId(rezervare),
                    getNume(rezervare),
                    tipClasa,
                    getPret(rezervare),
                    getCheckin(rezervare)
                )
                listaNoua.append(rezervareNoua2)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def ieftinireRezervare(procentCitit, lista):
    """
    Ieftinirea tuturor rezervarilor cu un procent citit la care s a facut checkin-ul
    :param procentCitit: un int
    :param lista: o lista
    :return: o lista de rezervari
    """
    if procentCitit < 0:
        raise ValueError("Procentul nu poate fi mai mica decat 0!")
    listaNoua = []
    for rezervare in lista:
        if getCheckin(rezervare) == "DA":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare) - getPret(rezervare)//100*procentCitit,
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def pretMaximPeClase(lista):
    """
     Determinarea prețului maxim pentru fiecare clasă.
    :param lista: o lista
    :return: Preturile maxime pentru fiecare clasa
    """
    listaPret = [0, 0, 0]
    for rezervare in lista:
        clasa = getClasa(rezervare)
        pret = float(getPret(rezervare))
        if clasa == "economy":
            if listaPret[0] < pret:
                listaPret[0] = pret
        elif clasa == "economy plus":
            if listaPret[1] < pret:
                listaPret[1] = pret
        elif clasa == "business":
            if listaPret[2] < pret:
                listaPret[2] = pret
    if listaPret[0] == 0:
        listaPret[0] = "Nu exista rezervare la clasa economy"
    if listaPret[1] == 0:
        listaPret[1] = "Nu exista rezervare la clasa economy plus"
    if listaPret[2] == 0:
        listaPret[2] = "Nu exista rezervare la clasa business"

    return listaPret


def pretRezervare(rezervare):
    return getPret(rezervare)


def ordonareDescrescator(lista):
    """
    Ordonarea rezervărilor descrescător după preț.
    :param lista: o lista
    :return: lista ordonata dupa pret
    """
    return sorted(lista, key=pretRezervare, reverse=True)


def sumaDupaNume(lista):
    """
    Afișarea sumelor prețurilor pentru fiecare nume.
    :param lista: o lista
    :return: suma prețurilor pentru fiecare nume
    """
    rezultat = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat
