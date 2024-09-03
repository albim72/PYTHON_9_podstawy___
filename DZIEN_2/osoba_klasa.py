class Osoba:
    #opis stanu
    #new odpowiada za utworzenie nowej klasy
    def __new__(cls, *args, **kwargs):
        return object.__new__(Osoba)

    #init odpowiada a opis przyszłego obiektu
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek
        self.kolor_oczu = "brązowy"
        print(self.msg("Nowa klasa: "))

    #reprezentacja tekstowa obiektu
    def __repr__(self):
        return f"obiekt {id(self)} -> osoba {self.imie}"

    #opis zachowania
    def powitanie(self):
        print(f"Witaj, nazywam się {self.imie} i mam {self.wiek} lat, "
              f"kolor oczu: {self.kolor_oczu}")

    def msg(self,info):
        return f"{info} - klasa {self.__class__.__name__}"

#obiekty oparte na klasie Osoba
os1 = Osoba("Jan",56)
print(os1)
os1.powitanie()

os2 = Osoba("Anna",32)
os2.kolor_oczu = "niebieski"
print(os2)
os2.powitanie()

os3 = Osoba("Leon",21)
print(os3)
os3.powitanie()
