#zbiór - set - nawias tworzący zbiór {}
drzewa = {"dąb","sosna","klon","brzoza","topola","jesion","cyprys"}
print(f"drzewa: {drzewa}")
print(f"drzewa: {drzewa}")
print(f"drzewa: {drzewa}")

# for d in drzewa:
#     print(d)

#operacje na zbiorach
#dodawanie elementu
drzewa.add("modrzew")
print(f"drzewa: {drzewa}")

#usuwanie elementu ze zbioru
drzewa.remove("sosna")
print(f"drzewa: {drzewa}")

# drzewa.remove("buk")
drzewa.discard("buk")
print(f"drzewa: {drzewa}")

#sprawdzenie czy element jest w zbiorze
czy_jest = "dąb" in drzewa
print(f"czy dab jest w zbiorze? {czy_jest}")

#opercje na zbiorach: suma,przecięcie,różnica
inne_drzewa = {"buk","jodła","topola","klon"}

#suma
suma = drzewa | inne_drzewa
print(suma)

#przecięcie -  częśc wspólna zbiorów
przeciecie = drzewa & inne_drzewa
print(przeciecie)

#różnica zbiorów - elementy które są w zbiorze drzewa ale nie ma ich w inne_drzewa
roznica = drzewa - inne_drzewa
print(roznica)

#różnica symetryczna - elementy które są w jednym zbiorze lub drugim ale nie ma ich w obu jednocześnie
roz_symetryczna = drzewa ^ inne_drzewa
print(roz_symetryczna)

nb = [5,2,67,3,2,1,5,64,7,33,56,33,2,2,2,6,8,2,33,1,56]
