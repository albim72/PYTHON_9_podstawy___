from kolekcja import KolekcjaElementow

if __name__ == '__main__':
    kolekcja1 = KolekcjaElementow([1,3,5,7,8,9,10])
    kolekcja2 = KolekcjaElementow([103,7,81,-4])

    #repr
    print(kolekcja1)
    print(kolekcja2)

    #len
    print(len(kolekcja1))

    #getitem
    print(kolekcja1[2])

    #add
    kolekcja3 = kolekcja1 + kolekcja2
    print(kolekcja3)

    #mul
    kolekcja4 = kolekcja1 * 2
    print(kolekcja4)
