#klasa reprezentująca silnik samochodu
class Engine:
    def __init__(self,power):
        self.power = power

    def start(self):
        return f"Silnik o mocy {self.power} KM został uruchomiony...."

#klasa reprezentująca koło
class Wheel:
    def __init__(self,size):
        self.size = size

    def roll(self):
        return f"Koło o rozmiarze {self.size} cali - toczy się"

#klasa reprezentująca samochód!
class Car:
    def __init__(self,make,model,engine_power,wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(engine_power) #kompozycja - samochód posiada silnik
        self.wheels = [Wheel(wheel_size) for _ in range(4)] #kompozycja - samochód ma 4 koła

    def start_car(self):
        engine_status = self.engine.start()
        wheels_status = " ".join([wheel.roll() for wheel in self.wheels])
        return f"{engine_status}\n{wheels_status}"

myCar = Car(make="Toyota",model="Corolla",engine_power=150,wheel_size=17)

print(myCar.start_car())
