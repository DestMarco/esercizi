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