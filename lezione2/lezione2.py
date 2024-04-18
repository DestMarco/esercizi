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



