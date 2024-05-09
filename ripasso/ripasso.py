class person:

    def __init__(self,name:str,username:str,data_di_nascita,genere) -> None:
        self.name:str=name
        self.username:str=username
        self.data_di_nascita: str=data_di_nascita
        self.genere:str=genere

    def calcola_eta(self)->int:
        return 10

persona1=person(name="Marco",username="De Stefano",data_di_nascita="14/10/04",genere="Maschio")

print(persona1.calcola_eta())

class Dipendente(person):

    def __init__(self, name: str, username: str, data_di_nascita, genere) -> None:

        super().__init__(name, username, data_di_nascita, genere)
    def calcola_stipendio(self)->float:
        return 500.0

dipendente1=Dipendente(name="Marco",username="De Stefano",data_di_nascita="14/10/04",genere="Maschio")



print(persona1.calcola_eta())
print(dipendente1.name)
print(dipendente1.calcola_eta())
print(dipendente1.calcola_stipendio())