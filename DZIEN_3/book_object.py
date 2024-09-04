class Book:
    wydawnictwo:str

    def __init__(self,id,tytul,autor,cena=30):
        self.id = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def create_book(self):
        print("utworzenie nowej książki!")


bk = Book(45,"Wiedźmin","Andrzej Sapkowski",45)
print(bk)

