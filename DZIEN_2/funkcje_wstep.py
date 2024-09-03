#przykład 1 - podstawowa funkcja nbez aargumentów i bez zwracania wartości
def wypisz_dzien_dobry():
    print("Powitanie - Hej to ja - funkcja!")

wypisz_dzien_dobry()
wypisz_dzien_dobry()
wypisz_dzien_dobry()

#przykład 2 - podstawowa funkcja nbez aargumentów i ze zwracaniem wartości

def pisz_kolor():
    return "kolor podstawowy -> biały!"

print(pisz_kolor())
powitanie = pisz_kolor() + " Drugi kolor -> czarny..."
print(powitanie)

#przykład 3 - podstawowa funkcja z argumentami i bez zwracania wartości
def dodaj_wartosci(a,b,c):
    wynik = a+b+c
    print(f"suma a+b+c wynosi: {wynik}")

dodaj_wartosci(3,6,78)
dodaj_wartosci(1,0,.78)
dodaj_wartosci(-76,100,9.999)
dodaj_wartosci(True,True,False)
dodaj_wartosci(45,True,-12)

#przykład 4 - podstawowa funkcja z argumentami i ze zwracaniem wartości
def policz_cos(w,k,p):
    return (w+2*k)/p

print(policz_cos(3,5,7))
wynik = 505 + policz_cos(1,2,3)
print(wynik)

#przykład 5 - funkcja z wartościami domyślnymi
#name - imię osoby
#greetings  - tekst pozdrowień
#sign - znak interpunkcyjny na końcu wypowiedzi...
def greet(name,greetings = "Witaj",sign="."):
    print(f"{greetings} {name}{sign}")

greet("Anna")
greet("Olaf","Sie ma")
greet("Olaf","Sie ma","!")
greet("Maria",sign="!!!")

#przykład 6 - funkcja z arbitralną liczbą argumentów
# *args -> lista argumentów o dowolnej dlugości
def pomnoz(*args):
    wynik = 1
    for num in args:
        wynik *= num
    return wynik

print(pomnoz(4,1,8))
print(pomnoz(8,19,1,3,5,78,4))
print(pomnoz(4.77,1,3.009))
print(pomnoz(4))
print(pomnoz())
print(pomnoz("gsdf"))


#przykład 7 - funkcja z dokumentacją
"""
ważny komentarz
"""

def skladowe_liczby(a,b):
    """
    opis składowych w obliczeniu odejmowania a-b
    :param a: wartośc całkowita dodatnia
    :param b: wartośc całkowita doadtnia lub zmiennoprzecinkowa nieujemna
    :return: wynik w typie int lub float (numbers)
    """

    """
    drugi komentarz dla a-b!
    """

    return a-b
print("odejmowanie a-b:")
print(skladowe_liczby(6,4))
print(skladowe_liczby.__doc__)

#pierwszy komnentarz w  otwartej strukturze kodu jest
#komentarzem dokumentacyjnym (automatycznie jest przekazywany do dokumentacji)
