kraje = ["Polska","Szwecja","Słowacja","Niemcy","Hiszpania","Irlandia","Beligia"] #lista kraje - symbol []
#wyświetlenie listy
print(kraje)
print(kraje[1]) #wyśweitlenie elementu o indeksie 1
print(kraje[2:4]) #wy świetlenie 2 i 3 elementu listy, czwarty nie zwiera się w przedziale
#zakresy -> lewostrronnie zawiera się, prawostronnike nie zawiera
print(kraje[2:7:2]) # kraje[od:do:skok]
print(kraje[:6])
print(kraje[4:])

kraje.append("Włochy") #dodawanie elementu listy na końcu listy
print(kraje)

kraje.insert(4,"Litwa") #dodawanie elementu na konkretnym miejscu (4)
print(kraje)
kraje.sort() #sortowanie A-Z
print(kraje)
kraje.reverse() #odwrócenie kolejności w liście
print(kraje)

liczby = [2,4,56,78,-9,0,12,-45,0,98,24,51,25,29,221,-116]
print(liczby)
liczby.sort(reverse=True) #sortowanie odwrotne Z-A
print(liczby)
liczby.remove(-9) #usuwanie elementu - pierwsza wartośc od lewej strony
print(liczby)

powtorzenie = [2,3,5,6,8,3,9,6,4,3,2,5,7,4,3,5,3,6,3]

