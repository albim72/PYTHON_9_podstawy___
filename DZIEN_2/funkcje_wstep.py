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
