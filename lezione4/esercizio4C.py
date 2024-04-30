"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what
you are learning about in this chapter. Call the function, and make sure the message displays correctly.
"""
def display_message():
    print("In this chapter we learn how to make functions in Python.")

# Call the function to display the message
display_message()

print("------------------------------------------------------------")

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title.
The function should print a message, such as "One of my favorite books is Alice in Wonderland".
Call the function, making sure to include a book title as an argument in the function call.
"""

def favorite_book(title):
    print(f"One of my favorite books is{title}")
# Call the function with a book title
favorite_book("Testa Cucita")


print("------------------------------------------------------------")
"""
8-3. T-Shirt: Write a function called make_shirt()
that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
ùCall the function once
using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""

def make_shirt(size, message):
    print(f"Creating a {size} shirt with the message {message}")

# Call the function using positional arguments
make_shirt("medium", "one piece is real")

# Call the function using keyword arguments
make_shirt(size="large", message="i am iron man")

print("------------------------------------------------------------")

"""
8-4. Large Shirts: Modify the make_shirt()
function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size="large", message="I love Python"):
    print("Creating a", size, "shirt with the message:", message)

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", message="have you ever praised the sun")


print("------------------------------------------------------------")


"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter
for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
"""

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("New York")
describe_city("Tokyo", "Japan")

print("------------------------------------------------------------")

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this: "Santiago, Chile".
Call your function with at least three city-country pairs, and print the values that are returned.
"""

def city_country(city, country):
    return city + ", " + country

# Call the function with three city-country pairs
print(city_country("Reykjavik", "Iceland"))
print(city_country("New York", "USA"))
print(city_country("Tokyo", "Japan"))


print("------------------------------------------------------------")

"""
8-7. Album: Write a function called make_album() that builds a dictionary 
ùdescribing a music album. The function should take in an artist name and an album title,
and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums.
Print each return value to show that the  dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs 
on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
Make at least one new function call that includes the number of songs on an album.
"""

def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

# Make three dictionaries representing different albums
album1 = make_album("Michael Jackson", "Thriller")
album2 = make_album("Mystery Skulls", "The Future")
album3 = make_album("TheFatRat", "hiding in the blue")

# Print each dictionary
print(album1)
print(album2)
print(album3)


print("------------------------------------------------------------")
"""
8-8. User Albums: Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s
input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
"""



def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\nEnter album details (enter 'q' to quit):")
    artist = input("Artist: ")
    if artist.lower() == 'q':
        break
    title = input("Title: ")
    if title.lower() == 'q':
        break
    songs_input = input("Number of songs (optional, press Enter to skip): ")
    if songs_input.lower() == 'q':
        break
    if songs_input:
        songs = int(songs_input)
        album = make_album(artist, title, songs)
    else:
        album = make_album(artist, title)
    print("Album details:", album)
    
    
print("------------------------------------------------------------")

"""
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
"""

def show_messages(messages):
    for message in messages:
        print(message)

# List of short text messages
text_messages = [
    "Hello prise the sun !",
    "the one pice is real ",
    "UwU Sun .",
    "Have a great day!"
]

# Call the function to print the messages
show_messages(text_messages)


print("------------------------------------------------------------")
"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message to 
a new list called sent_messages as it’s printed. After calling the function,
print both of your lists to make sure the messages were moved correctly.
"""


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print("Sending message:", current_message)
        sent_messages.append(current_message)

# List of short text messages
text_messages = [
    "Hello prise the sun !",
    "the one pice is real ",
    "UwU Sun .",
    "Have a great day!"
]

# Empty list to store sent messages
sent_messages = []

# Call the function to send messages
send_messages(text_messages, sent_messages)

# Print both lists to verify messages were moved correctly
print("\nOriginal messages list:")
print(text_messages)

print("\nSent messages list:")
print(sent_messages)


print("------------------------------------------------------------")

"""
8-11. Archived Messages: Start with your work from Exercise 8-10. 
ùCall the function send_messages() with a copy of the list of messages. After calling the function, 
print both of your lists to show that the original list has retained its messages.
"""

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print("Sending message:", current_message)
        sent_messages.append(current_message)

# List of short text messages
text_messages = [
    "Hello prise the sun !",
    "the one pice is real ",
    "UwU Sun .",
    "Have a great day!"
]


# Empty list to store sent messages
sent_messages = []

# Call the function to send messages with a copy of the original list
send_messages(text_messages[:], sent_messages)

# Print both lists to show that the original list has retained its messages
print("\nOriginal messages list:")
print(text_messages)

print("\nSent messages list:")
print(sent_messages)

print("------------------------------------------------------------")
"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered.
Call the function three times, using a different number of arguments each time.
"""

def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("-", item)

# Call the function three times with a different number of arguments each time
make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Swiss cheese", "Tomato", "Mustard")
make_sandwich("Tuna", "Mayonnaise")


print("------------------------------------------------------------")


"""
8-13. User Profile:  Build a profile of yourself by calling build_profile(),
using your first and last names and three other key-value pairs that describe you.
All the values must be passed to the function as parameters.
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
"""

def build_profile(first_name, last_name, **kwargs):
    profile = f"{first_name} {last_name}"
    for key, value in kwargs.items():
        profile += f", {key} {value}"
    return profile

# Call the function to create a profile
my_profile = build_profile("Marco", "De Stefano", age=19, hair="light brown", weight=100)

# Print the profile
print(my_profile)

print("------------------------------------------------------------")
"""
8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. It should then accept an arbitrary 
number of keyword arguments. Call the function with the required information and two other name-value pairs, 
such as a color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True) 
Print the dictionary that’s returned to make sure all the information was stored correctly. 
"""

def make_car(manufacturer, model, **kwargs):
    c_f = {'manufacturer': manufacturer, 'model': model}
    for key, value in kwargs.items():
        c_f[key] = value
    return c_f

# Call the function with required information and additional name-value pairs
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the dictionary returned to verify all information was stored correctly
print(car)

print("------------------------------------------------------------")
"""
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.
py.Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
"""

# printing_functions.py

def print_models(models):
    """Simulate printing each design."""
    print("Printing models:")
    for model in models:
        print("- " + model)
print_models("hello word")

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print("- " + completed_model)
        

print("------------------------------------------------------------")

"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file.
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import 
"""


"""
import care
# main_program.py

# Approach 1: import module_name


car1 = car.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)

# Approach 2: from module_name import function_name
from care import make_car

car2 = make_car('toyota', 'camry', color='red', tow_package=False)
print(car2)

# Approach 3: from module_name import function_name as fn
from care import make_car as create_car

car3 = create_car('honda', 'civic', color='green', tow_package=True)
print(car3)

# Approach 4: import module_name as mn
import care as cf

car4 = cf.make_car('ford', 'focus', color='black', tow_package=False)
print(car4)

# Approach 5: from module_name import *
from care import *

car5 = make_car('chevrolet', 'malibu', color='white', tow_package=True)
print(car5)
"""

print("-------------------------------------------------------------------")

"""
8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.
"""
# create a fuction whit the artist and the name of test
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album

# Make three dictionaries representing different albums
album1:str = make_album("Michael Jackson", "Thriller")
album2:str = make_album("Mystery Skulls", "The Future")
album3:str = make_album("TheFatRat", "hiding in the blue")

# Print each dictionary
print(album1)
print(album2)
print(album3)

print("-------------------------------------------------------------------")


#create a fuction whit my favorite book
def favorite_book(title):
    print(f"One of my favorite books is{title}")
    
# Call the function with a book title
favorite_book("Testa Cucita")


print("-------------------------------------------------------------------")

# create a fuction tat print the sandwich 
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("-", item)

# Call the function three times with a different number of arguments each time
make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Swiss cheese", "Tomato", "Mustard")
make_sandwich("Tuna", "Mayonnaise")