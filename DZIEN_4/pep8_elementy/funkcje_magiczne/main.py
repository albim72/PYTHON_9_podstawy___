import math
from singleton import Singleton
from licznik_call import Licznikwywolan,FunkcjaLiniowa
from punkty_abs import Punkt

if __name__ == '__main__':
    #klasa jednoinstancyjna math
    m1 = math
    m11 = m1.sin(4)
    print(m11)
    print(id(m1))

    # m2 = math
    m12 = m1.pi
    print(m12)
    # print(id(m2))
    #
    # print(m1 is m2)

    #test działania klasy Singleton
    ob1 = Singleton()
    ob2 = Singleton()

    print(ob1 is ob2)

    ob1.dane = "Zmieniono dane!"

    print(f'dane obiekt ob1 -> {ob1.dane}')
    print(f'dane obiekt ob2 -> {ob2.dane}')

    # test działania klasy Licznikwywolan
    licznik = Licznikwywolan()

    print("\nwykoanie funkcji __call__ - obiekt zachowuje się jak funkcja")
    licznik()
    licznik()
    licznik()
    licznik()

    # test działania klasy FunkcjaLiniowa
    print("\nfunkcja liniowa:")
    funkcja = FunkcjaLiniowa(2,3)
    print(funkcja(5))
    print(funkcja(15))

    # test działania klasy Punkt
    punkt1 = Punkt(3,4)
    print(punkt1)

    odleglosc1 = abs(punkt1)
    print(f"odległośc punktu od (0,0) wynosi: {odleglosc1}")

    punkt2 = Punkt(-11, 9)
    print(punkt2)

    odleglosc2 = abs(punkt2)
    print(f"odległośc punktu od (0,0) wynosi: {odleglosc2}")
