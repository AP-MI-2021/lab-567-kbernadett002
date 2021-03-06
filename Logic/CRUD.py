from Domain.rezervare import creeazaRezervare, getId


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    """
    Adauga o rezervare intr-o lista
    :param id:string
    :param nume:string
    :param clasa:string
    :param pret:float
    :param checkin:string
    :param lista: Lista de rezervare
    :return: o lista care contine atat elementele vechi, cat si noua rezervare
    """
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if pret < 0:
        raise ValueError("Pretul nu poate fi negativ!")
    if clasa != "economy":
        if clasa != "economy plus":
            if clasa != "business":
                raise ValueError("Clasa incorecta!Reincercati")
    if checkin != "DA":
        if checkin != "NU":
            raise ValueError("Ati introdus gresit optiunea de checkin!Reincercati!")
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def getById(id, lista):
    """
    Da rezervarea cu id-ul dat
    :param id:float
    :param lista: lista de rezervare
    :return: rezervarea cu id-ul dat din lista sau None in cazul in care asta nu exista
    """
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None


def stergereRezervare(id, lista):
    """
    Sterge rezervarea cu id-ul dat
    :param id: string
    :param lista:o lista de rezervare
    :return: o lista de rezervari
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista rezervarea cu id-ul dat")
    return [rezervare for rezervare in lista if getId(rezervare) != id]


def modificareRezervare(id, nume, clasa, pret, checkin, lista):
    """
    Modifica o prajitura dupa id
    :param id:string
    :param nume:string
    :param clasa:string
    :param pret:float
    :param checkin:string
    :param lista:o lista de rezervare
    :return: o rezervare modificata
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista rezervarea cu id-ul dat")
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua
