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

#CTRL+/  - komentowanie/odkomentowanie linii kodu (bloku)
#CTRL + D - duplikat linii/bloku kodu

# lista_bez_duplikatow = []
# for element in powtorzenie:
#     if element not in lista_bez_duplikatow:
#         lista_bez_duplikatow.append(element)
# lista_bez_duplikatow.remove(3)
# print(powtorzenie)
# print(lista_bez_duplikatow)

wartosc = 3
p2 = powtorzenie.copy()
for element in p2:
    if element == 3:
        p2.remove(wartosc)

print(powtorzenie)
print(p2)

sklepzoo = [["pies","kot","papuga","mysz"],[4500,2500,900,45]]
print(sklepzoo[0])
print(sklepzoo[0][1])
print(sklepzoo[0][1], "-",  sklepzoo[1][1])

sklepzoo_2 = [[["buldog angielski","Wyżeł Weimarski","Owczarek Podhalański"],"kot","papuga","mysz"],
            [[7500,6500,4500],2500,900,45]]

print(sklepzoo_2[0][0][0],"-",sklepzoo_2[1][0][0])

