
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
class user:
    def __init__ (self, first_name:str, last_name:str, age:int, cf:int, email:str):
        self.sirst_name=first_name
        self.last_name=last_name
        self.age=age
        self.cf=cf
        self.email=email

    def greet_user(self):
        print(f"Hello {self.sirst_name}. come va?")
    def __str__(self) ->str:
        return f"User(name={self.sirst_name})"\
        +f"username={ self.last_name}"
user1= user(first_name="Lorenzo",
            age=22, last_name="Maggi",
            email="lorenzo.maggi@gmail.com",
            cf="MGGLNZ01L07H50IL")
print(user)

print("------------------------------------------------------------------------------------")
