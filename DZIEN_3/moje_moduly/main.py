# import dane
# import dane as dn
from dane import nrfilii as nf
from dane import book as bk

from funkcje.bfunkcje import czytaj_liste,czytaj_slownik

print("______ dane bezpośrednie ______")
print(nf)
print(bk)

print("\n______ wyświetlanie z użyciem funkcji ______")
czytaj_liste(nf)
czytaj_slownik(bk)
