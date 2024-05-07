"""
class Persona:
    def __init__(self,name:str,username:str, age:int) :
        self.name=name
        self.username=username
        self.age=age

lorenzo=Persona("Lorenzo","Maggi", 25)
print(f'Nome={lorenzo.name}, Cognome={lorenzo.username}, Age={lorenzo.age}')
lorenzo.age=22
print(f'Età={lorenzo.age}')

danila=Persona("Danila","Rahautsou",21)
print(f'Nome={danila.name}, Cognome={danila.username}, Age={danila.age}')


name:str=input()
username:str=input()
age:int =int(input())

person=Persona(name,username,age)
print(f'Persona con nome={person.name}, cognome={person.username}, eta={person.age}')
"""
class Person:
    def __init__(self,name:str, age:int) :
        self.name=name
        self.age=age
alice=Person("Alice W.",45)
bob=Person("Bob M.",36)

print(bob.age)

if alice.age > bob.age:
    print(alice.age)
else:
    print(bob.age)
andrea=Person("Andrea B.",20)
riccardo=Person("Riccardo G.",27)
giovanni=Person("Giovanni D.",21)

people=[alice,bob,andrea,riccardo,giovanni]
c=None
for i in people:
    if c == None:
        c = i.age
    if c > i.age:
        c=i.age
print(c)

print("------------------------------------------------------------------------------------------")

class Student:
    def __init__ (self, name:str,studyProgram:str, age:int, gender:str):
        self.name= name 
        self.studyprogram=studyProgram
        self.age=age
        self.gender=gender 

    def print_info(self):
        print(f"Name={self.name}, study Program={self.studyprogram}, age={self.age},"\
              +f" gender={self.gender}")
        
        
        

myself=Student("Marco","Informatics",19,"M")
l_n=Student("Riccardo","Computer science",27,"M")
r_n=Student("Andrea","Informatics",20,"M")

myself.print_info()
print()
l_n.print_info()
print()
r_n.print_info()
print()


