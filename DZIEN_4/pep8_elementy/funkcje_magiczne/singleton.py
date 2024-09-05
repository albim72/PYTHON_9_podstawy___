class Singleton:
    _instancja = None #atrybut klasy do przechowywania jednej instancji
    
    def __new__(cls):
        if cls._instancja is None:
            # jeśli instancja jeszcze nie istnieje, tworzy nowy obiekt
            cls._instancja = super().__new__(cls)
        return cls._instancja
    
    def __init__(self):
        self.dane = "jestem jedyną instancją klasy Singleton!"
