import pickle

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, my name is {self.name} and I'm {self.age} years old."

#tworzymy obiekt klasy Person
person = Person("Alice",30)

#serializujemy obiekt i zapisujemy do pliku person.pkl

with open('person.pkl','wb') as file:
    pickle.dump(person,file)

print("obiekt został zapisany do pliku - person.pkl!")

with open('person.pkl','rb') as file:
    loaded_person = pickle.load(file)

#sprwdzenie czy obiekt jest poprawnie załadowany
print("odczytano obiekt")
print(loaded_person.greet())
