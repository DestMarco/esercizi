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