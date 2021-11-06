from Tests.testAll import runAllTests
from UserInterface.UImodificat import meniu
from UserInterface.console import runMenu


def print_utilizare():
    print("Alegeti tipul de meniu folosit: ")
    print("1. Meniul vechi")
    print("2. Meniul nou")


def main():
    lista = []
    runAllTests()
    print_utilizare()
    optiune = input("Dati optiunea: ")
    if optiune == "1":
        runMenu(lista)
    elif optiune == "2":
        meniu(lista)
    else:
        print("Optiune gresita!Reincercati!")


if __name__ == '__main__':
    main()
