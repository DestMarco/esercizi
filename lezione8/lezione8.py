"""
class Animal:
    def __init__(self,specie:str,età:int,nome:str):
        self.specie=specie
        self.età=età
        self.nome=nome
    def __str__(self) -> str:
        return f'{self.__class__.__name__}(name{self.nome},specie={self.specie}, eta={self.età})'
class Person(Animal):
    def __init__(self, età: int,surname:str, nome:str,cod_fiscale:str, specie="Homo Sapiens"):
        super().__init__(specie, età)
        self.nome=nome
        self.cod_fiscale=cod_fiscale
        self.surname=surname
    def __str__(self) -> str:
        return f"{self.nome.capitalize()}{self.surname.capitalize()}(cf={self.cod_fiscale})"\
            + f",age={self.età}"\
            + f",specie={self.specie}"

class Studente(Person):
    def __init__(self, età: int, surname:str ,nome: str, cod_fiscale: str, N_ma:str ,specie="Homo Sapience"):
        super().__init__(età, nome, cod_fiscale, specie)
        self.N_ma=N_ma    
    
class Gat(Animal):
    def __init__(self,  età: int,nome:str,specie="Felidae"):
        super().__init__(specie, età)
        self.nome=nome
    def __str__(self) -> str:
        return f"name={self.nome},eta={self.età}, specie={self.specie}"
class Rabit(Animal):
    def __init__(self, età: int,nome:str , specie="Leporidae"):
        super().__init__(specie, età)
        self.nome=nome
    def __str__(self) -> str:
        return f"nome={self.nome},age={self.età},specie={self.specie}"

P=Person(nome="lorenzo",surname="Maggi",cod_fiscale="bella",età=22,specie="Homo Sapiens")
a=Animal(nome="willi",specie="Balaen Balana",età=25)
print(P)
print(a)
c= Gat(nome="Garfield",età=15,specie="Felidae")
print(c)
"""
print("----------------------------------------------------------------------------------------------------------")
class Rooms:
    def __init__(self,id:str,floor:int,seats:int):
          self.id=id
          self.floor=floor
          self.seats=seats
    def get_floor(self):
         return self.floor
    def get_seats(self):
         return self.seats
    def get_id(self):
         return self.id
    def __str__(self) -> str:
         return f"Rooms=(id={self.id},floor={self.floor},seats={self.seats})"
        
class Bulding:
    def __init__(self,name:str,num_float:str,address:str,rooms:list=[Rooms]) -> None:
        self.name=name
        self.address=address
        self.num_float=num_float
        self.rooms:list [Rooms]=rooms
    def get_num_float(self):
         return self.num_float
    def get_rooms(self):
         return self.rooms
    def add_room(self,room:Rooms):
         if room not in self.rooms\
          and room.get_floor() <= self.get_num_float():
              self.rooms.append(room)
    def __str__(self):
            return f"{self.name.capitalize()}@{self.address}"
smi=Bulding(name="SMI",address="via sierra nevada à60",num_float=5)
smi.add_room(id="666",floor=3,seats=32)


