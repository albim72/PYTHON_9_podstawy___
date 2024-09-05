class Liczby:
    def __init__(self,liczby):
        self.liczby = liczby
        
    def __invert__(self):
        """Odwraca znaki wszystkich liczb w liście"""
        return Liczby([-liczba for liczba in self.liczby])
    
    def __repr__(self):
        return f"Liczby({self.liczby})"
