class KolekcjaElementow:
    def __init__(self,elementy):
        """inicjacja kolekcji z listą elementów"""
        self.elementy = elementy
        
    def __repr__(self):
        """reprezentacja obiektu"""
        return f"KolekcjaElementow({self.elementy})"
    
    def __len__(self):
        """zwraca liczbę elementow kolekcji"""
        return len(self.elementy)
    
    def __getitem__(self, index):
        """pozwala na dostęp do elementu o podanym indeksie"""
        return self.elementy[index]
    
    def __add__(self, other):
        """dodaje dwie kolekcje przez połączenie elementów - konkatenacja"""
        if isinstance(other,KolekcjaElementow):
            return KolekcjaElementow(self.elementy + other.elementy)
        return NotImplemented
    
    def __mul__(self, mnoznik):
        """mnożenie elementów kolekcji przez podaną liczbę"""
        if isinstance(mnoznik,int):
            return KolekcjaElementow(self.elementy*mnoznik)
        return NotImplemented
    
    
