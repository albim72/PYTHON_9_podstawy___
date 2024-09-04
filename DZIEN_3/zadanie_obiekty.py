class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def wykonaj_zadanie(self):
        print("Osoba wykonuje zadanie.")

class Sportowiec:
    def __init__(self, dyscyplina, wynik):
        self.dyscyplina = dyscyplina
        self.wynik = wynik

    def wykonaj_zadanie(self):
        print("Sportowiec wykonuje zadanie.")

class Zawodnik(Osoba, Sportowiec):
    def __init__(self, imie, nazwisko, dyscyplina, wynik):
        Osoba.__init__(self, imie, nazwisko)
        Sportowiec.__init__(self, dyscyplina, wynik)

    def przedstaw_siebie(self):
        return f"{self.imie} {self.nazwisko}, dyscyplina: {self.dyscyplina}, wynik: {self.wynik}"

    def wykonaj_zadanie(self):
        print(f"Zawodnik wykonuje zadanie w dyscyplinie: {self.dyscyplina}.")

# Tworzenie dwóch obiektów klasy Zawodnik
zawodnik1 = Zawodnik("Anna", "Kowalska", "Lekkoatletyka", 12.34)
zawodnik2 = Zawodnik("Jan", "Nowak", "Pływanie", 54.21)

# Wyświetlanie przedstawień zawodników
print(zawodnik1.przedstaw_siebie())
print(zawodnik2.przedstaw_siebie())

zawodnik1.wykonaj_zadanie()  # Zawodnik wykonuje zadanie w dyscyplinie: Lekkoatletyka.
zawodnik2.wykonaj_zadanie()  # Zawodnik wykonuje zadanie w dyscyplinie: Pływanie.

os = Osoba("Karol","Boryna")
os.wykonaj_zadanie()

sp = Sportowiec("biegi ultra","100km 12:34:12")
sp.wykonaj_zadanie()
