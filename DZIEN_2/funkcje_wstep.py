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
