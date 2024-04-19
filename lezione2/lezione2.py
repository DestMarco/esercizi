#Marco Destefano
#18/04/2024
print("Hello word")
"""
Personal Message: Use a variable to represent a person’s 
name, and print a message to that person. Your message should
 be simple, such as, “Hello Eric, would you like to learn some Python today?”
"""
#questa variabbile contiene il nome 
name:str="Mario"
#questa variabbile contine il messagio
message:str=f"Ciao{name}, ti va di imparare un pò di python insime? "
print(message)


"""
2-4. Name Cases: Use a variable to represent a person’s name, and 
then print that person’s name in lowercase, uppercase, and title case.
"""
#questa variabbile contiene il nome 
name: str="Mario"
#questa variabbile contine il nome in caratteri minuscoli
name_lower:str=name.lower()
#questa variabbile contine il nome in caratteri magliuscole
name_upper:str=name.upper()

print(f"{name},{name_upper},{name_lower} ")


"""
2-5. Famous Quote: Find a quote from a famous person you admire. 
Print the quote and the name of its author. 
Your output should look something like the following, 
including the quotation marks: Albert Einstein once said, “A person who 
never made a mistake never tried anything new.”
"""
#questa variabbile contiene il nome della celebrità
N:str="The Rok"
#questa variabbile contiene la frase della celebrità
Frase:str="\" Chi mi fa pressione me lo mangio a colazione \""
print(f"{N}\n{Frase}")

"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, 
represent the famous person’s name using a variable called famous_person. 
Then compose your message and represent it with a new variable called message. 
Print your message. 
"""
#questa variabbile contiene il nome della celebrità
Famus_Name:str="The Rok"
#questa variabbile contiene la frase della celebrità
Messaggio:str="\" Chi mi fa pressione me lo mangio a colazione \""
print(f"{N}\n stampa il messagio \n{Messaggio}")

"""
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix().
Assign the value 'python_notes.txt' to a variable called filename. 
Then use the removesuffix() method to display the filename without the file extension, 
like some file browsers do.
"""
#questa variabbile una stringa con .txt
file_name:str="python-notes.txt"
#questa variabbile rimuove il .txt alla vecchia variabbile 
file_Remuve:str=file_name.removesuffix(".txt")

print(f"{file_Remuve}")


"""
3-1. Names: Store the names of a few of your friends in a list called names.
 Print each person’s name by accessing each element in the list, one at a time.
"""
#è una lista che cotiene un elenco dei nomi dei mie amici
Nome_amici:list=["Andrea","Damiano","Rafel","Giovanni","Manuel"]

print(f"{Nome_amici[0]} \n {Nome_amici[1]} \n {Nome_amici[2]} \n {Nome_amici[3]} \n {Nome_amici[4]}")

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, 
but instead of just printing each person’s name, print a message to them.
 The text of each message should be the same, 
 but each message should be personalized with the person’s name.
"""

#è una lista che cotiene un elenco dei nomi dei mie amici
Nome_amici:list=["Andrea","Damiano","Rafel","Giovanni","Manuel"]
Messagio_A:str="Ciao come stai"

print(f"{Messagio_A} {Nome_amici[0]} \n {Messagio_A} {Nome_amici[1]} \n {Messagio_A} {Nome_amici[2]} \n {Messagio_A} {Nome_amici[3]} \n {Messagio_A} {Nome_amici[4]}")

"""
3-3. Your Own List: Think of your favorite mode of transportation, 
such as a motorcycle or a car, and make a list that stores several examples.
 Use your list to print a series of statements about these items, 
such as “I would like to own a Honda motorcycle.”
"""
Lista:list=["Ford Mustang","Doge Challenger","Bugatti","Lamborghini"]

mes:str="ma non ho i soldi"

for i in range (len(Lista)):
    print(f"vorrei {Lista[i]} {mes}")


 