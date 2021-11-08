from Domain.rezervare import getId
from Logic.CRUD import adaugaRezervare


def testUndoRedo():
    undoList = []
    redoList = []
    lista = []

    add = adaugaRezervare('1', 'Ana', 'economy', 200, 'DA', lista)
    undoList.append(lista)
    lista = add

    add = adaugaRezervare('2', 'Costel', 'economy plus', 250, 'DA', lista)
    undoList.append(lista)
    lista = add

    add = adaugaRezervare('3', 'Relu', 'business', 500, 'NU', lista)
    undoList.append(lista)
    lista = add

    assert getId(lista[0]) == '1'
    assert getId(lista[1]) == '2'
    assert getId(lista[2]) == '3'

    redoList.append(lista)
    lista = undoList.pop()
    assert getId(lista[0]) == '1'
    assert getId(lista[1]) == '2'
    assert len(lista) == 2

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == '1'
    assert undoList == [[]]

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == []

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList
    assert len(lista) == 0
    assert undoList == []

    add = adaugaRezervare('1', 'Mihai', 'economy', 200, 'NU', lista)
    undoList.append(lista)
    lista = add
    redoList.clear()

    add = adaugaRezervare('2', 'Aurica', 'economy plus', 300, 'DA', lista)
    undoList.append(lista)
    lista = add

    add = adaugaRezervare('3', 'Gigel', 'economy', 200, 'DA', lista)
    undoList.append(lista)
    lista = add

    assert len(undoList) == 3
    assert len(redoList) == 0
    assert len(lista) == 3

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[0]) == "1"
    assert getId(lista[1]) == "2"

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == '1'
    assert undoList == [[]]

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2
    assert len(redoList) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 3
    assert len(undoList) == 3
    assert len(redoList) == 0

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[0]) == '1'
    assert getId(lista[1]) == '2'

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == '1'
    assert undoList == [[]]

    add = adaugaRezervare('4', 'Ionel', 'economy plus', 200, 'DA', lista)
    undoList.append(lista)
    lista = add
    redoList.clear()

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(undoList) == 2
    assert len(lista) == 2

    redoList.append(lista)
    lista = undoList.pop()
    assert len(undoList) == 1
    assert len(redoList) == 1
    assert len(lista) == 1

    redoList.append(lista)
    lista = undoList.pop()
    assert len(undoList) == 0
    assert len(redoList) == 2
    assert len(lista) == 0

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista =redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(undoList) == 2
    assert len(redoList) == 0
    assert len(lista) == 2


