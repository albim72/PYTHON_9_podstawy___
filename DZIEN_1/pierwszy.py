print("to jest wstęp do języka Python!")
tekst = "to jest zmienna typu tesktowego -> str"
print(tekst)

#liczba calkowita (int)
liczba_calk = 10
print("liczba stałoprzecinkowa:",liczba_calk,"zmienna typu:",type(liczba_calk))
opis = "f-string"

print(f"struktura ekstrapolacji ciągów str w postaci {opis}")

#liczba zmiennoprzecinkowa (float)
liczba_zm = 19.89
print(f"liczba zmiennoprzecinkowa: {liczba_zm}, zmienna typu: {type(liczba_zm)}")

#liczba zespolona (complex)
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

