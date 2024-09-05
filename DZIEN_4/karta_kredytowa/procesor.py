from abc import ABC,abstractmethod

class ProcesorPlatnosci(ABC):
    @abstractmethod
    def autoryzuj(self):
        """
        metoda abstrakcyjna, która będzie implementowana w klasach pochodnych - obowiązkowo
        :return: pass (brak ciała metody)
        """
        pass

    @abstractmethod
    def przetworz_platnosc(self,kwota):
        pass

    
