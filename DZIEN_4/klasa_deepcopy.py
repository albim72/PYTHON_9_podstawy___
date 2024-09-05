import copy

class MojaKopia:
    def __init__(self,nazwa):
        self.nazwa = nazwa

    def __deepcopy__(self, memo):
        print(f"tworzenie kopii głębokiej obiektu parametru klasy MojaKopia: {self.nazwa}")
        nowy_obiekt = self.__class__(self.nazwa)
        memo[id(self)] = nowy_obiekt
        return nowy_obiekt

oryginal = MojaKopia("taki tam tekst - kilka literek...")
skopiowany = copy.deepcopy(oryginal)
print(oryginal)
print(skopiowany)

print("drugi obiekt")
oryginal2 = MojaKopia([3,6,2,6,2,6])
skopiowany2 = copy.deepcopy(oryginal2)
print(oryginal2)
print(skopiowany2)

print(f"oryginalny obiekt przed kopiowaniem: {oryginal2}")
oryginal2.nazwa = [4234,53463,6765]
print(f"oryginalny obiekt po zmianie kolekcji: {oryginal2}")
skopiowany2 = copy.deepcopy(oryginal2)
print(f"kopia obiektu po zmianie kolekcji: {skopiowany2}")

mojstr = "taki tam tekst - kilka literek..."
print(mojstr)
print(mojstr[2:6])



