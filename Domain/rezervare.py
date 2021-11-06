def creeazaRezervare(id, nume, clasa, pret, checkin):
    """
    Creeaza un dictionar ce reprezinta o rezervare
    :param id: un string
    :param nume:un string
    :param clasa:un string
    :param pret:float
    :param checkin:un string
    :return: un dictionar ce reprezinta o rezervare
    """
    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }


def getId(rezervare):
    """
    Da id-ul unei rezervari
    :param rezervare:un dictionar ce contine o rezervare
    :return: id-ul unei rezervari
    """
    return rezervare["id"]


def getNume(rezervare):
    """
    Da numele unei rezervari
    :param rezervare: un dictionar ce contine o rezervare
    :return: numele unei rezervari
    """
    return rezervare["nume"]


def getClasa(rezervare):
    """
    Da clasa unei rezervari
    :param rezervare: un dictionar ce contine o rezervare
    :return: clasa unei rezervari
    """
    return rezervare["clasa"]


def getPret(rezervare):
    """
    Da pretul unei rezervari
    :param rezervare: un dictionar ce contine o rezervare
    :return: pretul unei rezervari
    """
    return rezervare["pret"]


def getCheckin(rezervare):
    """
    Determina daca este facut checkin-ul
    :param rezervare:un dictionar ce contine o rezervare
    :return:daca s a fcaut checkin-ul sau nu
    """
    return rezervare["checkin"]


def toString(rezervare):
    """
    Da o rezervare
    :param rezervare: un dictionar
    :return: o rezervare
    """

    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )
