#przykład 1  - podstawowa klasa Rectangle
class Rectangle:
    #funkcja init() definiuje przyszłe obiekty
    #wpisanie danych: width,height towrzy obowiązek podania tych wartości dla każdego obiektu
    """
    Klasa Rectangle - definiująca obiekt prostokąt - reprezentacja figury geometrycznej
    width - bok podstawy prostokąta
    height - bok wysokości prostokąta

    """
    #konstruktor klasy
    def __init__(self,width,height):
        self.width = width
        self.height = height

    #pole prostokąta
    def area(self):
        return self.width*self.height

    #obwód prostokąta
    def perimeter(self):
        return 2*(self.width+self.height)

print("*"*70)
print("\033[4;34mPrzykład 1\033[0m")
#tworzenie obiektu
rect = Rectangle(12,7)
print(f'Pole prostokąta: {rect.area()} cm2')
print(f'Obwód prostokąta: {rect.perimeter()} cm')

#tworzenie drugiego obiektu - prostokąt o23
o23 = Rectangle(2,5)
print(f'Pole prostokąta: {o23.area()} cm2')
print(f'Obwód prostokąta: {o23.perimeter()} cm')

print(Rectangle.__doc__)


#przykład 2  - klasa z domyślnymi wartościami i metodą specjalną __str__

class Rectangle:
    #konstruktor klasy
    def __init__(self,width=1,height=1):
        self.width = width
        self.height = height

    #pole prostokąta
    def area(self):
        return self.width*self.height

    #obwód prostokąta
    def perimeter(self):
        return 2*(self.width+self.height)

    def __str__(self):
        return f"Rectangle(width = {self.width} cm, height = {self.height} cm)"

print("*"*70)
print("\033[4;34mPrzykład 2\033[0m")
rec1 = Rectangle()
print(rec1)
print(f'Pole prostokąta: {rec1.area()} cm2')
print(f'Obwód prostokąta: {rec1.perimeter()} cm')

rec2= Rectangle(68,26)
print(rec2)
print(f'Pole prostokąta: {rec2.area()} cm2')
print(f'Obwód prostokąta: {rec2.perimeter()} cm')

