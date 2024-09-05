import copy

oryginalny_obiekt = {
    'a':1,
    'b':[2,3,{'c':4,'d':[5,6]}],
    'c':100
}

mobiekt = oryginalny_obiekt

sobiekt = oryginalny_obiekt.copy()
print(sobiekt)

kobiekt = copy.deepcopy(oryginalny_obiekt)
print(kobiekt)

oryginalny_obiekt['b'][2]['c'] = 99
oryginalny_obiekt['b'][0] = 0
oryginalny_obiekt['b'][2]['d'][0] = 0.0005
oryginalny_obiekt['a']=True
oryginalny_obiekt['c']="setka"

print("nastąiły zmiany\n")
print(oryginalny_obiekt)
print("przypisanie do nowej zmiennej: mobiekt")
print(mobiekt)
print("kopia zwykła")
print(sobiekt)
print("kopia głęboka")
print(kobiekt)


