from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testTrecereClasaSuperioara, testSumaDupaNume, testOrdonareDescrescator


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testTrecereClasaSuperioara()
    testSumaDupaNume()
    testOrdonareDescrescator()
