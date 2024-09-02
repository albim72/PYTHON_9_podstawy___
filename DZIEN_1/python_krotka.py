animal = ("pies","kot","papuga","królik","szczur","pies")

print(animal)
#krotka = ()
print(type(animal))
print(animal[3])
print(animal[2:5])

print(animal.index("papuga"))
print(animal.count("pies"))

for a in animal:
    print(a)

if "papuga" in animal:
    print("Tak! papuga to zwierz!")

animal = animal + ("budynek",)
print(animal)

if "budynek" in animal:
    print("Nie! bydnek nie nalezy do zwierząt!")

