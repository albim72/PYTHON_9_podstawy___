def czytaj_liste(lista):
    print(f"___ lista {lista} ___")
    for i,j in enumerate(lista):
        print(f"element listy nr {i+1} -> wartośc: {j}")

def czytaj_slownik(slownik):
    print(f"___ słownik {slownik} ___")
    for x,y in slownik.items():
        print(f"klucz: {x} -> wartośc: {y}")
