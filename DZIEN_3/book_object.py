class Book:
    wydawnictwo:str

    def __init__(self,id,tytul,autor,cena=30):
        self.id = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.__oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return f"Książka: {self.tytul}, {self.autor} -> cena: {self.cena} zł"

    def create_book(self):
        print("utworzenie nowej książki!")

    def get_oprawa(self):
        return self.__oprawa

    def set_oprawa(self,nowaoprawa):
        self.__oprawa = nowaoprawa

    def rabat(self,procent):
        return self.cena*(procent/100)

    def set_wydawnictwo(self,nazwa):
        self.wydawnictwo = nazwa

    def get_wydawnictwo(self):
        return self.wydawnictwo


bk = Book(45,"Wiedźmin","Andrzej Sapkowski",45)
print(bk)
#tworzenie zupełnie nowej zmiennej oprawa, raczej nie powieniśmy w tym wypadku kreaowa nowej zmiennej
#alternatywnej dla __oprawa
# bk.oprawa = "twarda"
# print(f"oprawa: {bk.oprawa}")
print(f"zmienna __oprawa: {bk.get_oprawa()}")
print("zmiana oprawy!")
bk.set_oprawa("twarda")
print(f"nowa oprawa: {bk.get_oprawa()}")
print(f"rabat od ceny: {bk.rabat(15)} zł")
bk.set_wydawnictwo("ABC")
print(f"wydawnictwo: {bk.get_wydawnictwo()}")



