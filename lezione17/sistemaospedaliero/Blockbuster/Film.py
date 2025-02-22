"""In un file chiamato "film.py", si definisca la 
classe Film che rappresenta un film preso a nolleggio. In tale classe, 
definire un codice identificativo (int) ed un titolo (string). Entrambi gli 
attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
"""

class Film:
    def __init__(self,id:int,title:str) :
            self.id=id
            self.title=title

    def setId(self,id):
          self.id=id
    def setTitle(self,title):
          self.title=title
    def getId(self):
          return self.id
    def getTitle(self):
          return self.title
    def isEqual(self,otherFilm):
          return self.id == otherFilm.getId()