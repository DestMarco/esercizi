class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating an instance of the Restaurant class
restaurant = Restaurant("The Great Feast", "Italian")

# Printing individual attributes
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("----------------------------------------------------------------------------------")
"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant() for each instance.
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating three instances of the Restaurant class
restaurant1 = Restaurant("The Great Feast", "Italian")
restaurant2 = Restaurant("Spice Delight", "Indian")
restaurant3 = Restaurant("Sushi Paradise", "Japanese")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
print("----------------------------------------------------------------------------------")
"""
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several 
other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
 Create several instances representing different users, and call both methods for each user.
"""
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
       
    
    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}! UwU.")

# Creating instances of the User class

user1 = User("Andre", "Bardi", 20)


# Calling methods for each user
user1.describe_user()
user1.greet_user()

print("----------------------------------------------------------------------------------")

"""
9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and
print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a
new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
"""
class Restaurant:
    def __init__(self, ristorante: str, cucina: str, num: int = 0) -> None:
        self.ris = ristorante
        self.cuc = cucina
        self.num_served = num
    
    def describe_restaurant(self):
        print(f"Nome ristorante: {self.ris}, cucina di tipo {self.cuc}\n")
    
    def open_restaurant(self):
        print(f"Il nuovo ristorante {self.ris} è aperto!")
    
    def set_num_served(self, new_number_served: int):
        self.num_served = new_number_served 
    
    def increment_number(self):
        self.num_served += 1
    
    def increment_number_served(self, increment: int):
        self.num_served += increment

# Creating an instance of the Restaurant class
r3 = Restaurant(ristorante="Da Baffo", cucina="romana", num=2)

# Printing the initial number of customers served
print("Initial number of customers served:", r3.num_served)

# Setting a new number of customers served
r3.set_num_served(4)
print("Number of customers served after setting:", r3.num_served)

# Incrementing the number of customers served
r3.increment_number_served(10)  # Incrementing by 10
print("Number of customers served after incrementing:", r3.num_served)


print("----------------------------------------------------------------------------------")

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3.
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several 
times. Print the value of login_attempts to make sure it was incremented properly,
and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
"""


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}! UwU.")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating an instance of the User class
user1 = User("Andre", "Bardi", 20)

# Calling methods for the user
user1.describe_user()
user1.greet_user()

# Incrementing login attempts multiple times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Printing login attempts to ensure it's correctly incremented
print("Login attempts:", user1.login_attempts)

# Resetting login attempts
user1.reset_login_attempts()

# Printing login attempts again to ensure it's reset to 0
print("Login attempts after reset:", user1.login_attempts)

print("----------------------------------------------------------------------------------")

"""
- 9-6. Ice Cream Stand: Un supporto per gelati è un tipo specifico di ristorante. Scrivi una classe chiamata
IceCreamStand che eredita dalla classe del ristorante che hai scritto in Esercizio 9-1 o Esercizio 9-4. Entrambe
le versioni della classe funzioneranno; basta scegliere quello che ti piace di più. Aggiungi un attributo chiamato 
sapori che memorizza una lista di aromi di gelato.
Scrivi un metodo che mostri questi sapori. Creare un'istanza di IceCreamStand e chiamare questo metodo.
"""



class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(flavor)

# Creating an instance of the IceCreamStand class
ice_cream_stand = IceCreamStand("The Frozen Spoon", "Ice Cream Parlor")
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

# Calling the method to display flavors
ice_cream_stand.display_flavors()

print("----------------------------------------------------------------------------------")
"""
9-7. Admin: An administrator is a special 
kind of user. Write a class called Admin that inherits from 
the User class you wrote in Exercise 9-3 or Exercise 9-5. Add 
an attribute, privileges, that stores a list of strings like 
"can add post", "can delete post", "can ban user", and so 
on. Write a method called show_privileges() that lists the 
administrator’s set of privileges. Create an instance of 
Admin, and call your method. 
"""

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}!")


class Admin(User):  # La classe Admin eredita dalla classe User
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)  # Chiama il costruttore della classe genitore
        self.privileges = privileges  # Aggiunge l'attributo privileges
    
    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Creazione di un'istanza di Admin
admin1 = Admin("John", "Doe", 30, ["can add post", "can delete post", "can ban user"])
user1 = User("Andre", "Bardi", 20)
# Chiamata dei metodi della classe User tramite l'istanza di Admin
admin1.describe_user()
admin1.greet_user()

# Chiamata del metodo specifico della classe Admin
admin1.show_privileges()

user1.describe_user()
user1.greet_user()
print("----------------------------------------------------------------------------------")

"""
9-8. Privileges: Write a separate Privileges class. The class should have one attribute,
privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges()
method to this class. Make a Privileges instance as an attribute in the Admin class.
Create a new instance of Admin and use your method to show its privileges.
"""
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}!")

class Admin(User,Privileges):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)  # Utilizza la classe Privileges come attributo
    
    def show_privileges(self):
        self.privileges.show_privileges()  # Chiama il metodo show_privileges() della classe Privileges

# Creazione di un'istanza di Admin con le relative Privileges
admin1 = Admin("John", "Doe", 30, ["can add post", "can delete post", "can ban user"])
user1 = User("Andre", "Bardi", 20)
# Utilizzo del metodo show_privileges() dell'istanza di Admin
admin1.show_privileges()
            
user1.describe_user()
user1.greet_user()

print("----------------------------------------------------------------------------------")

"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working properly.
"""

from ristorante import Restaurant

# Creazione di un'istanza della classe Restaurant
r3 = Restaurant(ristorante="Da Baffo", cucina="romana", num=2)

# Stampa del numero iniziale di clienti serviti
print("Numero iniziale di clienti serviti:", r3.num_served)

# Impostazione di un nuovo numero di clienti serviti
r3.set_num_served(4)
print("Numero di clienti serviti dopo l'impostazione:", r3.num_served)

# Incremento del numero di clienti serviti
r3.increment_number_served(10)  # Incremento di 10
print("Numero di clienti serviti dopo l'incremento:", r3.num_served)

print("----------------------------------------------------------------------------------")

"""
9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges,
and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() 
to show that everything is working correctly.
"""
from admin import Admin, User
# Creazione di un'istanza di Admin con le relative Privileges
admin1 = Admin("John", "Doe", 30, ["can add post", "can delete post", "can ban user"])
user1 = User("Andre", "Bardi", 20)
# Utilizzo del metodo show_privileges() dell'istanza di Admin
admin1.show_privileges()
            
user1.describe_user()
user1.greet_user()


print("----------------------------------------------------------------------------------")
"""
9-12. Multiple Modules: Store the User class in one module, and store
the Privileges and Admin classes in a separate module. In a separate file, 
create an Admin instance and call 
show_privileges() to show that everything is still working correctly.
"""
from Adpre import User,Privileges
from user import User
# Creazione di un'istanza di Admin
admin1 = Admin("John", "Doe", 30, ["can add post", "can delete post", "can ban user"])
user1 = User("Andre", "Bardi", 20)
# Chiamata dei metodi della classe User tramite l'istanza di Admin
admin1.describe_user()
admin1.greet_user()

# Chiamata del metodo specifico della classe Admin
admin1.show_privileges()

user1.describe_user()
user1.greet_user()


print("----------------------------------------------------------------------------------")

"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
Make a 6-sided die and roll it 10 times. 
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(f"Rolling a {self.sides}-sided die:")
        for _ in range(10):
            roll = random.randint(1, self.sides)
            print(f"Roll: {roll}")

# Creazione di un dado a 6 facce e lancio 10 volte
six_sided_die = Die()
six_sided_die.roll_die()

# Creazione di un dado a 10 facce e lancio 10 volte
ten_sided_die = Die(sides=10)
ten_sided_die.roll_die()

# Creazione di un dado a 20 facce e lancio 10 volte
twenty_sided_die = Die(sides=20)
twenty_sided_die.roll_die()


print("----------------------------------------------------------------------------------")

"""
9-14. Lottery: Make a list or tuple containing a 
series of 10 numbers and 5 letters. Randomly select 4 
numbers or letters from the list and print a message saying that 
any ticket matching these 4 numbers or letters wins a prize.

"""

import random

# Definizione della lista contenente numeri e lettere
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Estrazione casuale di 4 numeri o lettere dalla lista
winning_combination = random.sample(lottery, k=4)

# Stampa della combinazione vincente
print("La combinazione vincente è:", winning_combination)
print("Ogni biglietto che corrisponde a questi 4 numeri o lettere vince un premio!")

print("------------------------------------------------------------------------")

"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind
of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps
pulling numbers until your ticket wins.
Print a message reporting how many times the loop had to run to give you a winning ticket.
"""

import random

# Funzione per generare un biglietto casuale
def generate_ticket():
    lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
    return random.sample(lottery, k=4)

# Biglietto da cercare
my_ticket = [8, 'D', 10, 1]

# Contatore dei tentativi
attempts = 0

# Loop finché non viene trovato un biglietto vincente
while True:
    attempts += 1
    if generate_ticket() == my_ticket:
        break

# Stampa del numero di tentativi necessari per vincere
print(f"Sono stati necessari {attempts} tentativi per vincere con il biglietto {my_ticket}.")