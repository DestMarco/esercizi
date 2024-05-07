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

print("------------------------------------------------------------------------------------------")

class Animal:
    def __init__ (self, name:str, legs:int):
        self.name=name
        self.legs=legs
        
    def set_legs (self,legs):
        self.legs=legs

    def get_legs (self):
        return self.legs

    def print_info (self):
        print(f'Name ={self.name}, Legs ={self.legs}')

animal1=Animal("Dog", 4)
animal2=Animal("Snake", 0)


print(animal1.name)
print(animal2.name)

animal1.set_legs(3)

animal2.set_legs(100)

print(animal1.get_legs())
print(animal2.get_legs())

animal1.print_info()
animal2.print_info()

print("--------------------------------------------------------------------------")
class Food:
    def __init__(self, name:str, price: float, description=None):
        self.name=name
        self.price=price
        self.description=description
class Menu:
    def __init__(self, foods=None):
        if foods is None:
            self.foods=[]
        else:
            self.foods=foods
    def add_food(self, food:str):
        self.foods.append(food)
    def removeFood(self,food:str):
        for i in self.foods:
            if i.name == food:
                self.foods.remove(i)

food1=Food("pizza", 9.99)
food2=Food("burger", 10)
food3=Food("cavial",100)

menu = Menu([food1,food2,food3])

menu.add_food(Food("meat",20.90))
menu.add_food(Food("oro",70.69))

menu.removeFood("oro")






