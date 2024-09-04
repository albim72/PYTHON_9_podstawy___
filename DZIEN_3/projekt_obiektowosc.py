import math
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

#przykład 3  - dziedziczenie klasy Rectangle przez klasę Square
class Square(Rectangle):
    def __init__(self,side_length):
        super().__init__(side_length,side_length)

    def squarediagonal(self):
        return self.width*math.sqrt(2)

print("*"*70)
print("\033[4;34mPrzykład 3\033[0m")

square = Square(6)
print(square)
print(f'Pole kwadratu: {square.area()} cm2')
print(f'Obwód kwadratu: {square.perimeter()} cm')
print(f'Przekątna kwadratu: {square.squarediagonal():.3f} cm')

#przykład 4  - enkapsulacja - prywatne atrybuty
#ukrycie szczegółów implementacji przed użutkownikiem klasy - wystawienie metod!
class BankAccount:
    def __init__(self,balance,special_amount):
        self.__balance = balance
        self._special = special_amount

    #wpłata środków na konto
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    #wypłata środków z konta
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance -= amount

    #wyświetlanie stanu konta
    def get_balance(self):
        return self.__balance


print("*"*70)
print("\033[4;34mPrzykład 4\033[0m")

acc = BankAccount(800,100)
acc.deposit(1600)
print(f'stan konta po dokonaniu wpłaty: {acc.get_balance()} zł')
acc.withdraw(437)
print(f'stan konta po dokonaniu wypłaty: {acc.get_balance()} zł')
print("czy fizycznie zmienna __balance jest prywatna - niedostępna z poziomu programu??")
# print(acc.__balance)
# print(BankAccount.__balance)
print("nie ma dostępu do zmiennej __balance!!!")
print("Czy mam dostęp do _special?")
print(acc._special)
print("tak! _special daje dostęp obiektowi do siebie")
# _ - protected,  __ - private

#przykład 5  - polimorfizm - różne klasy z tą samą metodą!
class Dog:
    def speak(self):
        return "Hau!"

class Cat:
    def speak(self):
        return "Miau!"

class Cow:
    def speak(self):
        return "Muuu!"

#funkcja która wywołuje metodę speak
def animal_sound(animal):
    print(animal.speak())

#użycie polimorfizmu
print("*"*70)
print("\033[4;34mPrzykład 5\033[0m")

dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
