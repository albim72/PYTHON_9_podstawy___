print("to jest wstęp do języka Python!")
tekst = "to jest zmienna typu tesktowego -> str"
print(tekst)
# print to funkcja która wyświetla dane (wyniki) na ekranie w konsoli

#liczba calkowita (int)
liczba_calk = 10
#zmienne definiowane poprzez nazwy: liczba_calk nają przypisaną wartośc (znak przypisania =) a wartosc 10
print("liczba stałoprzecinkowa:",liczba_calk,"zmienna typu:",type(liczba_calk))
opis = "f-string" #rodzaj wyświetlania ciągu znaków z opcją wstrzyknięcia w nawiasach {} wyników, danych itd..
#funkcja type -> funkcja opisująca rodzaj danych (obiekt i jego klasa) np int - liczba całkowita lub str

print(f"struktura ekstrapolacji ciągów str w postaci {opis}")

#liczba zmiennoprzecinkowa (float)
liczba_zm = 19.89
print(f"liczba zmiennoprzecinkowa: {liczba_zm}, zmienna typu: {type(liczba_zm)}")
print("zwykły string -> {liczba_zm}")

#liczba zespolona (complex) - pierwiastek z liczb ujemnych
liczba_zesp = 2 + 3j
print(f"liczba zespolona: {liczba_zesp}, zmienna typu: {type(liczba_zesp)}")

#wartośc logiczna (bool)
wart_logiczna = True
print(f"wartośc logiczna: {wart_logiczna}, zmienna typu: {type(wart_logiczna)}")

#typ bajtowy (Bytes)
typ_bajt = b"Witaj typie Bajt!"
print(f"typ byte: {typ_bajt}, w typie {type(typ_bajt)}")

#przykład modyfikacji bytearray
typ_bytearray = bytearray(b'Witaj ByteArray!')
typ_bytearray[0] = 104 #kod ASCII litery h
print(f"zmodyfikowany type bytearray: {typ_bytearray}")

"""
komentarz dokumentacyjny wieloliniowy
linia2 - > dwa słowa
linia3 -> o dokumentacji....
xxxxx
33333
....
"""

a:int = 17 #definicja typu - int  - opisowa - to ozncza że mogę redefiniowac zmienną a w innym typie
print(a)
print(type(a))
print(id(a))

a = "liczba a" #redefinicja zmiennej a w typie str!
print(a)
print(type(a))
print(id(a))
