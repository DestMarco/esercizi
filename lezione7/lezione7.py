class Persona:
    def __init__(self,name:str,username:str, age:int) :
        self.name=name
        self.username=username
        self.age=age
"""
lorenzo=Persona("Lorenzo","Maggi", 25)
print(f'Nome={lorenzo.name}, Cognome={lorenzo.username}, Age={lorenzo.age}')
lorenzo.age=22
print(f'Età={lorenzo.age}')

danila=Persona("Danila","Rahautsou",21)
print(f'Nome={danila.name}, Cognome={danila.username}, Age={danila.age}')
"""

name:str=input()
username:str=input()
age:int =int(input())

person=Persona(name,username,age)
print(f'Persona con nome={person.name}, cognome={person.username}, eta={person.age}')
