from Domain.rezervare import getNume, getClasa, creeazaRezervare, getId, getPret, getCheckin


def trecereClasaSuperioara(numeCitit,lista):
    '''
    Trece toate rezervarile facute la un nume citit la o clasa superioara
    :param numeCitit: un string
    :param lista:o lista
    :return: o lista de rezervari
    '''
    listaNoua=[]
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
    '''
    Ieftinirea tuturor rezervarilor cu un procent citit la care s a facut checkin-ul
    :param procentCitit: un int
    :param lista: o lista
    :return: o lista de rezervari
    '''
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



