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

#tworzenie obiektu
rect = Rectangle(12,7)
print(f'Pole prostokąta: {rect.area()} cm2')
print(f'Obwód prostokąta: {rect.perimeter()} cm')

#tworzenie drugiego obiektu - prostokąt o23
o23 = Rectangle(2,5)
print(f'Pole prostokąta: {o23.area()} cm2')
print(f'Obwód prostokąta: {o23.perimeter()} cm')

print(Rectangle.__doc__)
