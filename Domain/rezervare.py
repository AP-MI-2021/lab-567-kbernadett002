def creeazaRezervare(id,nume,clasa,pret, checkin):
    '''
    Creeaza o lista ce reprezinta o rezervare
    :param id: un string
    :param nume:un string
    :param clasa:un string
    :param pret:float
    :param checkin:un string
    :return: o lista ce reprezinta o rezervare
    '''
    return [id, nume, clasa, pret, checkin]

def getId(rezervare):
    '''
    Da id-ul unei rezervari
    :param rezervare:o lista ce contine o rezervare
    :return: id-ul unei rezervari
    '''
    return rezervare[0]


def getNume(rezervare):
    '''
    Da numele unei rezervari
    :param rezervare: o lista ce contine o rezervare
    :return: numele unei rezervari
    '''
    return rezervare[1]


def getClasa(rezervare):
    '''
    Da clasa unei rezervari
    :param rezervare: o lista ce contine o rezervare
    :return: clasa unei rezervari
    '''
    return rezervare[2]


def getPret(rezervare):
    '''
    Da pretul unei rezervari
    :param rezervare: o lista ce contine o rezervare
    :return: pretul unei rezervari
    '''
    return rezervare[3]


def getCheckin(rezervare):
    '''
    Determina daca este facut checkin-ul
    :param rezervare:o lista ce contine o rezervare
    :return: Daca e facut checkin-ul sau nu
    '''
    return rezervare[4]


def toString(rezervare):
    '''
    Da o rezervare
    :param rezervare: o lista
    :return: o rezervare
    '''

    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )
