from abc import ABC, abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x = x

    #metoda nieabstrakcyjna
    def msg(self,info):
        return f'ważna informacja: {info}'

    #metody abstrakcyjne
    @abstractmethod
    def forma_chleb(self):
        pass

    @abstractmethod
    def forma_bagietka(self):
        pass

    @abstractmethod
    def forma_ciasto(self):
        pass

class Forma(Prototyp):
    def __init__(self,x,szer,wys,gl):
        super().__init__(x)
        self.szer = szer
        self.wys = wys
        self.gl = gl

    def forma_chleb(self):
        return f"materiał stal, wymiary: {self.szer} x {self.wys} x {self.gl}"

    def forma_bagietka(self):
        return f"materiał aluminium, wymiary: {self.szer} x {self.wys} x {self.gl}"

    def forma_ciasto(self):
        return f"materiał teflon, wymiary: {self.szer} x {self.wys} x {self.gl}"


pkr = Forma(450,34,12,12)
print(pkr.forma_chleb())
print(pkr.forma_bagietka())
print(pkr.forma_ciasto())
print(pkr.msg("foremka - AC1"))



