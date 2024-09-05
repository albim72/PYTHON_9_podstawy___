import math
from singleton import Singleton

if __name__ == '__main__':
    #klasa jednoinstancyjna math
    m1 = math
    m11 = m1.sin(4)
    print(m11)
    print(id(m1))

    # m2 = math
    m12 = m1.pi
    print(m12)
    # print(id(m2))
    #
    # print(m1 is m2)

    #test działania klasy Singleton
    ob1 = Singleton()
    ob2 = Singleton()

    print(ob1 is ob2)

    ob1.dane = "Zmieniono dane!"

    print(f'dane obiekt ob1 -> {ob1.dane}')
    print(f'dane obiekt ob2 -> {ob2.dane}')


