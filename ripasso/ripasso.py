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



