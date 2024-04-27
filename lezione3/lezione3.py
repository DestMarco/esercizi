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
favorite_pizzas = ['Pepperoni', 'spicy salami', '4 cheeses']

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
pizzas = ['Pepperoni', 'spicy salami', '4 cheeses']
apps = ['Nachos', 'Wings', 'Bruschetta']
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





    