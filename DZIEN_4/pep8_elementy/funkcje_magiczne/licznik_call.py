class Licznikwywolan:
    def __init__(self):
        self.liczba_wywolan = 0

    def __call__(self, *args, **kwargs):
        """Zwiększa licznik i wykonuje zadaną akcję..."""
        self.liczba_wywolan += 1
        print(f"funkcja została wywołana {self.liczba_wywolan} razy")


class FunkcjaLiniowa:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __call__(self, x):
        """zwraca wynik funkcji liniowek y = ax + b"""
        return self.a * x + self.b
    
