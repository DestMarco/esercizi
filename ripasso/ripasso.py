"""
class person:

    def __init__(self,name:str,
                 username:str,
                 data_di_nascita:str,
                 genere:str) -> None:
        
        self._name:str=name
        self.username:str=username
        self.data_di_nascita: str=data_di_nascita
        self.genere:str=genere

    def calcola_eta(self)->int:
        return 10
    def __eq__(self, value: object) -> bool:
      return value.get_name()=self._name



persona1=person(name="Marco",username="De Stefano",data_di_nascita="14/10/04",genere="Maschio")

print(persona1.calcola_eta())

persona1._name # non fare 
class Dipendente(person):

    def __init__(self, name: str,
                  username: str, data_di_nascita:str,
                    genere:str,
                    ore_lavorate:str) -> None:

        super().__init__(name, username, data_di_nascita, genere)
        self.ore_lavorate=ore_lavorate

    def calcola_stipendio(self)->float:
        return 500.0

dipendente1=Dipendente(name="Marco",username="De Stefano",data_di_nascita="14/10/04",genere="Maschio",ore_lavorate=500)


class professore(Dipendente):

    def __init__(self, name: str,
                  username: str,
                  data_di_nascita: str,
                  genere: str,
                  ore_lavorate: int,
                  materia_insegnata:str,
                  ore_di_lezione:int) -> None:
        
        super().__init__(name, username, data_di_nascita, genere, ore_lavorate)
        self.materia_insegnata:str=materia_insegnata
        self.ore_di_lezione=ore_di_lezione

professore1=professore(name="Marco",username="De Stefano",data_di_nascita="14/10/04",genere="Maschio",ore_lavorate=500,materia_insegnata="informatica",ore_di_lezione=100000)

print(persona1.calcola_eta())

print(dipendente1.ore_lavorate)
print(dipendente1.name)
print(dipendente1.calcola_eta())
print(dipendente1.calcola_stipendio())

print(professore1.materia_insegnata)
print(professore1.ore_di_lezione)
"""
"""
from abc import ABC, abstractmethod

class AbcAnimal(ABC):
 
    @abstractmethod
    def verso (self):
        pass
    @abstractmethod
    def movimento(self):
        pass



class Serpente(AbcAnimal):
    def __init__(self,nome) -> None:
        super().__init__()
        self.nome=nome
        self.velocita:float=10000000000000.0
    def verso(self):
        return print("psssss")
    def movimento(self, t):
        return self.velocita * t
       
Serpente_1:Serpente=Serpente(nome="Jormungandr")
Serpente_1.verso()
Serpente_1.movimento(t=1000000000000)


class gatto(AbcAnimal):
    def __init__(self,nome) -> None:
        super().__init__()
        self.nome=nome
        self.velocità=19.0
    def verso(self):
        return print("UwU")
    def movimento(self, t):
        return self.velocita * t
gatto_1:gatto=gatto(nome="franco")
gatto_1.verso()
gatto_1.movimento(t=10)
"""

class ContoBancario:
    total_account=0
    def __init__(self,iban, saldo, nome) -> None:
        self.iban=iban
        self.nome=nome
        self.saldo=saldo
        
        ContoBancario.total_account +=1
    def deposito(self, importo):
        self.importo=importo
        print(f"{importo} depositato. il nuovo saldo è{self.saldo}")
    def prelievo(self, importo):
        self.saldo -=importo
        print(f"{importo} prelevato. il nuovo saldo è {self.saldo}")
    @classmethod
    def get_total_accounts(cls):
        print(f"Account totali creati: {cls.total_account}")
    
    @staticmethod
    def valida_account(iban):
        if isinstance (iban, int) and len (str(iban)) == 10:
            print ("iban valido")
            return True
        else:
            print("iban non valido")
            return False
        
        
account1=ContoBancario(1234567890,0,'Alice')
account2=ContoBancario(9876543210,1000, 'Bob')

account1.prelievo(500)
account1.deposito(200)

account2.prelievo(200)
account2.deposito(100)

ContoBancario.get_total_accounts()

ContoBancario.valida_account(1234567890)
ContoBancario.valida_account('12345ABCD')


