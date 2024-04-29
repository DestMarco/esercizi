"""
Think of at least three kinds of your favorite pizza. Store these pizza names in a list, 
and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, 
instead of printing just the name of the pizza. For each pizza, 
you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop,
that states how much you like pizza. The output should consist of three or more lines about
the kinds of pizza you like and then an additional sentence,
such as I really love pizza!
"""
# List of favorite pizza
favorite_pizzas = ['Pepperoni', 'spicy salami', '4 cheeses']

# Print the names of each pizza
print("List of favorite pizzas:")
for pizza in favorite_pizzas:
    print(pizza)

# Print a sentence for each pizza
print("\nStatements about favorite pizzas:")
for pizza in favorite_pizzas:
    print("I like", pizza, "pizza.")

# Additional sentence
print("\nI really love pizza!")

print("-----------------------------------------------------------")

"""
4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common.
You could print a sentence, such as Any of these animals would make a great pet!
"""
# list of pets 
pets=["leopard gecko","snake","armadillo lizard"]

# print the animals 
print("\n print of pets")
for animals  in pets:
    print(f" {animals}")

# print a sentece of all pets
print("\n")
for animals in pets:
    print(f" {animals}, he would make a great pet!")
    
print("\n i love reptiles")

print("-----------------------------------------------------------")
"""
 Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
"""
# Print numbers from 1 to 20
print("Counting to Twenty:")
for number in range(1, 21):
    print(number)
    
print("-----------------------------------------------------------")

"""
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
"""
"""
# creating a list from 1 a 1 million
numbers = list(range(1, 1000001))

# Print the numbers using a for loop
for number in numbers:
    print(number)
"""
print("-----------------------------------------------------------")   

"""
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and ends at one million. Also,
use the sum() function to see how quickly Python can add a million numbers.
"""

total_sum = 0
minimum = None
maximum = None

# Generate numbers from one to one million and calculate the sum, minimum, and maximum
for number in range(1, 1000001):
    total_sum += number
    if minimum is None or number < minimum:
        minimum = number
    if maximum is None or number > maximum:
        maximum = number

# Print the results
print(f"Minimum number in the list{minimum}" )
print(f"Maximum number in the list{maximum}")
print(f"Sum of numbers from one to one million{total_sum}")

print("-----------------------------------------------------------")

"""
4-6. Odd Numbers: Use the third argument of the range()
function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
"""
# Make a list of odd numbers from 1 to 20
odd_numbers = list(range(1, 21, 2))

# Print each odd number
print("List of odd numbers from 1 to 20:")
for number in odd_numbers:
    print(number)

print("-----------------------------------------------------------")
"""
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
Use a for loop to print the numbers in your list.
"""

# Creating a list of multiples of 3 from 3 to 30
multiples_of_3 = [number for number in range(3, 31) if number % 3 == 0]

#Print numbers in the list using a for loop
print("List of multiples of 3 from 3 to 30:")
for multiple in multiples_of_3:
    print(multiple)
    
print("-----------------------------------------------------------")
"""
4-8. Cubes: A number raised to the third power is called a cube.
For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes
(that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
"""
# Make a list of the first 10 cubes
cubes = [number ** 3 for number in range(1, 11)]

# Print out the value of each cube using a for loop
print("Cubes of the first 10 integers:")
for i in cubes:
    print(i)
print("-----------------------------------------------------------")
"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
"""
# Initialize an empty list to store the cubes
cubes = []

# Generate the first 10 cubes using a for loop
for i in range(1, 11):
    cubes.append(i ** 3)

# Print the list of cubes
print("List of the first 10 cubes:")
print(cubes)

print("-----------------------------------------------------------")
"""
4-10. Slices: Using one of the programs you wrote in this chapter, 
add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:.
Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. 
Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:.
Then use a slice to print the last three items in the list.
"""

# Print numbers from 1 to 20
print("Counting to Twenty:")
for number in range(1, 21):
    print(number)

# Create a list of numbers from 1 to 20
numbers = list(range(1, 21))

# Print the message "The first three items in the list are:"
print("\n The first three items in the list are:")
for number in numbers[:3]:
    print(number)

# Print the message "Three items from the middle of the list are:"
print("\n Three items from the middle of the list are:")
m_s = len(numbers) // 2 - 1
m_e = m_s + 3
for number in numbers[m_s:m_e]:
    print(number)

# Print the message "The last three items in the list are:"
print("\n The last three items in the list are:")
for number in numbers[-3:]:
    print(number)
print("-----------------------------------------------------------")
"""
4-11. Le mie pizze, le tue pizze: inizia con il programma dell'esercizio 4-1.
Crea una copia dell'elenco delle pizze e chiamala friend_pizzas. Quindi, procedi come segue:
• Aggiungere una nuova pizza all'elenco originale.
• Aggiungi una pizza diversa alla lista friends_pizzas.
• Dimostra di avere due elenchi separati.
Stampa il messaggio Le mie pizze preferite sono:, quindi utilizza un ciclo for per stampare il primo elenco.
Stampa il messaggio Le pizze preferite del mio amico sono:,
quindi utilizza un ciclo for per stampare il secondo elenco. 
Assicurati che ogni nuova pizza sia memorizzata nell'elenco appropriato.
"""
# List of favorite pizza
favorite_pizzas = ["Pepperoni", "spicy salami", "4 cheeses"]

#create a copy of list list for my friend
f_p=favorite_pizzas[:]

# Add a new pizza to the original list
favorite_pizzas.append("lumberjack")
# Add a different pizza to your friend's list
f_p.append("margherita pizza")
# Print the names of each pizza
print("List of favorite pizzas:")
for pizza in favorite_pizzas:
    print(pizza)
# Print your friend's favorite pizzas
print("\nMy friend's favorite pizzas are:")
for pizza in f_p:
    print(pizza)
    
print("-----------------------------------------------------------")
"""
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing,
to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
"""
# List of favorite pizza
pizzas = ["Pepperoni", "spicy salami", "4 cheeses"]
apps = ["Nachos", "Wings", "Bruschetta"]
# Print the names of each pizza
print("List of pizzas:")
for pizza in favorite_pizzas:
    print(pizza)
    
print("\n")
    
for i in apps:
    print(i)

print("-----------------------------------------------------------")
"""
4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008.
You won’t use much of it now,
but it might be interesting to skim through it.
"""
print("-----------------------------------------------------------")
"""
4-15. Code Review: Choose three of the programs 
you’ve written in this chapter and modify each one to comply with PEP 8.
"""
# List of favorite pizza
favorite_pizzas = ["Pepperoni", "spicy salami", 
                   "4 cheeses", "Margherita Pizza" ]

# Print the names of each pizza
print("List of favorite pizzas:")
for pizza in favorite_pizzas:
     print(pizza)

# Print a sentence for each pizza
print("\nStatements about favorite pizzas:")
for pizza in favorite_pizzas:
     print("I like", pizza, "pizza.")

# Additional sentence
print("\nI really love pizza!")

print("----------------------------------------------------")

# Print numbers from 1 to 20
print("Counting to Twenty:")
for number in range(1, 21):
    print(number)
    
print("----------------------------------------------------")


# Make a list of odd numbers from 1 to 20
odd_numbers = list(range(1, 21, 2))

# Print each odd number
print("List of odd numbers from 1 to 20:")
for number in odd_numbers:
    print(number)

print("----------------------------------------------------") 
"""
Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
"""
car = 'nissan'
print("Is car == 'subaru'? I predict Fals.")
print(car == 'subaru')
print("\nIs car == 'nissan'? I predict True.")
print(car == 'nissan')

consol='Playstation4'
print("\nis consol == 'Playstation4'? I predict True")
print(consol=='Playstation4')
print("\nIs consol == 'Xbox'? I predict Fals.")
print(consol=='Xbox')

temperature = 25
print("\nIs temperature == 25? I predict True.")
print(temperature ==25)
print("\nIs temperature == 10? I predict False.")
print(temperature == 10)


name = 'John'
print("\nIs name == 'John'? I predict True.")
print(name == 'John')
print("\nIs name == 'Jane'? I predict False.")
print(name == 'Jane')

city = 'New York'
print("\nIs city == 'New York'? I predict True.")
print(city == 'New York')
print("\nIs city == 'Los Angeles'? I predict False.")
print(city == 'Los Angeles')

print("----------------------------------------------------") 
"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""
my_list = ['apple', 'banana', 'orange']
print("Verificare se un elemento è in un elenco:")
print('banana' in my_list)  
print('grape' in my_list)  
print("\nVerificare se un elemento non è in un elenco:")
print('grape' not in my_list)  
print('apple' not in my_list)  

temperature = 25
print("\nIs temperature > 20? I predict True.")
print(temperature > 20)
print("\nIs temperature < 10? I predict False.")
print(temperature < 10)


number1 = 10
number2 = 30
print("\nTest numerici:")
print("\nUguaglianza:", number1 == number2)  
print("\nDisuguaglianza:", number1 != number2)  
print("\nMaggiore di:", number1 > number2)  
print("\nMinore di:", number1 < number2)  
print("\nMaggiore o uguale a:", number1 >= number2)  
print("\nMinore o uguale a:", number1 <= number2) 

string1 = 'Hello Word'
string2 = 'hello word'
print("\nString equality test:")
print(string1 == string2)
print("\nString inequality test:")
print(string1 != string2)

# Test using the lower() method
print("\nTest using the lower() method:")
print(string1.lower() == string2)

print("----------------------------------------------------") 

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green.
If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. 
(The version that fails will have no output.)
"""

alien_color = 'green'

# Check if the alien's color is green
if alien_color == 'green':
    # Print a message that the player earned 5 points
    print("Congratulations! You just earned 5 points.")
print("--------------------------------------------------------")
alien_color = 'orange'

# Check if the alien's color is green
if alien_color == 'green':
    # Print a message that the player earned 5 points
    print("Congratulations! You just earned 5 points.")

print("--------------------------------------------------------")
"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
"""

# Assign a color to the alien
alien_color = 'green'

# Check if the alien's color is green
if alien_color == 'green':
    # Print a message that the player earned 5 points
    print("Congratulations! You just earned 5 points for shooting the green alien.")
else:
    # Print a message that the player earned 10 points
    print("Congratulations! You just earned 10 points for shooting the alien.")
    
print("--------------------------------------------------------")   


alien_color = 'orange'


if alien_color == 'green':
   
    print("Congratulations! You just earned 5 points for shooting the green alien.")
else:
  
    print("Congratulations! You just earned 10 points for shooting the alien.")
    
print("--------------------------------------------------------")
"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

# Assign a color to the alien
alien_color = 'green'

# Check if the alien's color is green
if alien_color == 'green':
    # Print a message that the player earned 5 points
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'orange':
    # Print a message that the player earned 10 points
    print("Congratulations! You just earned 10 points for shooting the orange alien.")
else:
      # Print a message that the player earned 15 points
     print("Congratulations! You just earned 15 points for shooting the red alien.")
     
print("--------------------------------------------------------")

# Assign a color to the alien
alien_color = 'orange'

# Check if the alien's color is green
if alien_color == 'green':
    # Print a message that the player earned 5 points
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'orange':
    # Print a message that the player earned 10 points
    print("Congratulations! You just earned 10 points for shooting the orange alien.")
else:
     # Print a message that the player earned 15 points
     print("Congratulations! You just earned 15 points for shooting the red alien.")
     
print("--------------------------------------------------------")
    
# Assign a color to the alien
alien_color = 'red'

# Check if the alien's color is green
if alien_color == 'green':
    # Print a message that the player earned 5 points
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == 'orange':
    # Print a message that the player earned 10 points
    print("Congratulations! You just earned 10 points for shooting the orange alien.")
else:
     # Print a message that the player earned 15 points
     print("Congratulations! You just earned 15 points for shooting the red alien.")
    
print("--------------------------------------------------------")

"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""
# Set the value for the variable age
age = 3

# Determine the person's stage of life using if-elif-else chain
if age < 2:
    print(" is a baby.")
elif age < 4:
    print(" is a toddler.")
elif age < 13:
    print(" is a kid.")
elif age < 20:
    print(" is a teenager.")
elif age < 65:
    print("is an adult.")
else:
    print(" is an elder.")
    
print("--------------------------------------------------------")
"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write
a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list.
If the fruit is in your list, the if block should print a statement, such as You really like Apples!
"""

# Make a list of your favorite fruits
favorite_fruits = ['apple', 'banana', 'mango', 'strawberry', 'orange']

# Write five independent if statements to check for certain fruits
if 'apple' in favorite_fruits:
    print("i really like the  Apples!")

if 'banana' in favorite_fruits:
    print("I really like banana!")

if 'mango' in favorite_fruits:
    print("I really like the Mangos because he is very sweet!")

if 'orange' in favorite_fruits:
    print("I like orange but not very much!")

if 'strawberry' in favorite_fruits:
    print("i really like Strawberries!")

print("--------------------------------------------------------")
"""
5-8. Hello Admin: Make a list of five or more usernames,
including the name 'admin'. Imagine you are writing code that will print a 
greeting to each user after they log in to a website. Loop through the list,
and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, 
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, 
thank you for logging in again.
"""
# Make a list of usernames
usernames = ['admin', 'Alice', 'Bob', 'Damiano', 'Andrea', 'Aurora']

# Loop through the list and print a greeting to each user
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
        
print("--------------------------------------------------------")
"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
"""

# Make a list of usernames
usernames = ['admin', 'Alice',
             'Bob', 'Damiano',
             'Andrea', 'Aurora']

# Check if the list of users is not empty
if usernames:
    # Loop through the list and print a greeting to each user
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Remove all usernames from the list
usernames.clear()

# Check if the list of users is now empty
if not usernames:
    print("We need to find some users!")
    
    
print("--------------------------------------------------------")
"""
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure
that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames
are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, 
print a message that the person will need to enter a new username.
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy 
of current_users containing the lowercase versions of all existing users.)
"""

# Make a list of current usernames
current_users = ['john', 'alice', 'bob', 'charlie', 'david']

# Make a list of new usernames
new_users = ['emily', 'Alice', 'mike', 'charlie', 'sarah']

# Loop through each new username
for new_user in new_users:
    # Check if the lowercase version of the new username is in the list of lowercase current usernames
    is_username_taken = False
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            is_username_taken = True
            break
    
    if is_username_taken:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")      
        

print("--------------------------------------------------------") 
"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, 
such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
"""
numbers = list(range(1, 10))

# Loop through the list
for number in numbers:
    # Check the last digit of the number to determine the ordinal ending
    if number == 1:
        #"st" is short for "first", which means "first" in English. It is used to indicate the first position in an ordered series.
        ordinal = 'st'
    elif number == 2:
        #"nd" is short for "second", which means "second" in English. It is used to indicate the second position in an ordered series.
        ordinal = 'nd'
    elif number == 3:
        #"rd" is short for "third", which means "third" in English. It is used to indicate the third position in an ordered series.
        ordinal = 'rd'
    else:
        #The abbreviation "th" is short for "th" in English, which is commonly used to denote most ordinals outside of the first three.
        ordinal = 'th'
    
    # Print the number with the appropriate ordinal ending
    print(f"{number}{ordinal}")