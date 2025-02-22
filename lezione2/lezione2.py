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
    
"""
If you could invite anyone, 
living or deceased, to dinner, 
who would you invite? Make a list that 
includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner.

"""    
print("--------------------------------------------------------------")
Lista1:list=["Andrea","Damiano","Giovanni"]



for i in range (len(Lista1)):
    print(f"vorrei invitarti a cena  {Lista1[i]} ")
    
    
    
print("---------------------------------------------------------------------")

Lista2 = ["Andrea", "Damiano", "Giovanni"]

# Printo la lista di invitati
for name in Lista2:
    print(f"Vorrei invitarti a cena, {name}.")

# Simulo una persona che non puo essere invitato
name_R = "Damiano"
print(f"\nscusa , {name_R} non pui venire a cena .\n")

# rimpiazzo il vecchio invitato
new_guest = "Chiara"
Lista2[Lista2.index(name_R)] = new_guest

# printo un nuovo messaggio
for name in Lista2:
    print(f"Vorrei invitarti a cena, {name}.")



print("---------------------------------------------------------------------")

# lista origginale 
guest_list = ["Andrea", "Damiano", "Giovanni"]


for name in guest_list:
    print(f"Vorrei invitarti a cena, {name}.")


print("\n ho trovato un tavolo piu' grande!\n")

# Aggiungo nuovi invitati
guest_list.insert(0, "Maria")  
guest_list.insert(len(guest_list) // 2, "Chiara") # serve a inserire il nome "Chiara" nella lista degli ospiti esattamente a metà della lista
guest_list.append("Luca") 

# Print nuovi invitati
for name in guest_list:
    print(f"Vorrei invitarti a cena, {name}.")
    
    
print("---------------------------------------------------------------------")


 # lista origginale
# Original guest list
guest_list = ["Andrea", "Damiano", "Giovanni", "Maria", "Chiara", "Luca"]

# Print lista iniziae 
print("Original guest list:")
for name in guest_list:
    print(f"Vorrei invitarti a cena, {name}.")

# Simulating the delayed arrival of the new dining table
print("\nscuste non posso invitare nessuno il tavolo mi arriva domani.\n")

# Remuovo dalla lista delle persone 
while len(guest_list) > 2:
    del guest_list[-1]
    print(f"Mi dispiace {guest_list[-1]}, ma non posso più invitarti a cena.")

# Print a person 
print("\nFinal guest list:")
for name in guest_list:
    print(f"Vorrei invitarti a cena, {name}.")

# lista vuota
del guest_list[:]
print("\nEmpty list after removing all guests:", guest_list)


print("---------------------------------------------------------------------")

# Lista originale
posti_da_visitare = ["Machu Picchu","Kyoto","Norveggia","Irlanda","Fiordi norvegessi"]

# Stampa l'elenco originale
print("Elenco originale:")
print(posti_da_visitare)

# Stampa l'elenco in ordine alfabetico senza modificarlo
print("\nElenco in ordine alfabetico:")
for posto in sorted(posti_da_visitare):
    print(posto)

# Stampa l'elenco ancora nell'ordine originale
print("\nElenco ancora nell'ordine originale:")
for posto in posti_da_visitare:
    print(posto)

# Stampa l'elenco in ordine alfabetico inverso senza modificarlo
print("\nElenco in ordine alfabetico inverso:")
for posto in sorted(posti_da_visitare, reverse=True):
    print(posto)

# Stampa l'elenco ancora nell'ordine originale
print("\nElenco ancora nell'ordine originale:")
for posto in posti_da_visitare:
    print(posto)

# Cambia l'ordine della lista
posti_da_visitare.reverse()
print("\nElenco con ordine invertito:")
for posto in posti_da_visitare:
    print(posto)

# Cambia nuovamente l'ordine della lista
posti_da_visitare.reverse()
print("\nElenco tornato all'ordine originale:")
for posto in posti_da_visitare:
    print(posto)

# Modifica l'elenco in ordine alfabetico
posti_da_visitare.sort()
print("\nElenco modificato in ordine alfabetico:")
for posto in posti_da_visitare:
    print(posto)

# Modifica l'elenco in ordine alfabetico inverso
posti_da_visitare.sort(reverse=True)
print("\nElenco modificato in ordine alfabetico inverso:")
for posto in posti_da_visitare:
    print(posto)
    
    
print("---------------------------------------------------------------------")


Lista2 = ["Andrea", "Damiano", "Giovanni"]

# Printo la lista di invitati
for name in Lista2:
    print(f"Vorrei invitarti a cena, {name}.")

# Simulo una persona che non può essere invitata
name_R = "Damiano"
print(f"\nScusa, {name_R} non può venire a cena.\n")

# Rimpiazzo il vecchio invitato
new_guest = "Chiara"
Lista2[Lista2.index(name_R)] = new_guest

# Printo un nuovo messaggio
for name in Lista2:
    print(f"Vorrei invitarti a cena, {name}.")

# Stampo il numero di persone invitate a cena
num_invitati = len(Lista2)
print(f"\nNumero di persone invitate a cena: {num_invitati}")


print("---------------------------------------------------------------------")

# Creazione di un elenco di montagne
montagne = ["Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu"]

# Stampa l'elenco originale
print("Elenco originale di montagne:")
print(montagne)

# Aggiungi una montagna alla fine dell'elenco
montagne.append("Cho Oyu")
print("\nMontagna aggiunta alla fine dell'elenco:")
print(montagne)

# Inserisci una montagna in una posizione specifica
montagne.insert(2, "Annapurna")
print("\nMontagna inserita in una posizione specifica:")
print(montagne)

# Rimuovi una montagna dall'elenco
montagne.remove("K2")
print("\nMontagna rimossa dall'elenco:")
print(montagne)

# Rimuovi l'ultima montagna dall'elenco
montagna_rimossa = montagne.pop()
print("\nUltima montagna rimossa dall'elenco:")
print(montagne)
print("Montagna rimossa:", montagna_rimossa)

# Trova la posizione di una montagna nell'elenco
posizione = montagne.index("Everest")
print("\nPosizione di Everest nell'elenco:", posizione)

# Conta quante volte una montagna appare nell'elenco
conteggio = montagne.count("Everest")
print("\nNumero di volte che Everest appare nell'elenco:", conteggio)

# Ordina l'elenco in ordine alfabetico
montagne.sort()
print("\nElenco di montagne ordinato in ordine alfabetico:")
print(montagne)

# Inverti l'ordine delle montagne nell'elenco
montagne.reverse()
print("\nElenco di montagne con ordine invertito:")
print(montagne)

# Copia l'elenco di montagne
copia_montagne = montagne.copy()
print("\nCopia dell'elenco di montagne:")
print(copia_montagne)

# Svuota l'elenco di montagne
montagne.clear()
print("\nElenco di montagne svuotato:")
print(montagne)


print("-------------------------------------------------------------------------------")

persona = {
    "nome": "Andrea",
    "cognome": "Bardi",
    "età": 20,
    "città": "Roma"
}

# Stampare ogni informazione memorizzata nel dizionario
print("Nome:", persona["nome"])
print("Cognome:", persona["cognome"])
print("Età:", persona["età"])
print("Città:", persona["città"])

print("-------------------------------------------------------------------------------")
"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary.
 Print each person’s name and their favorite number. 
For even more fun, poll a few friends and get some actual data for your program.
"""
favorite_number:dict={"Andrea":27,"Giovanni":47,"Gaia":3,"Frank":8,"Daniele":9}

for name,number in favorite_number.items():

    print(f"Il numero preferito di {name} è {number}.")
print("-------------------------------------------------------------------------------")
"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However,
 to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters.
 Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning,
 or print the word on one line and then print its meaning indented on a second line.
 Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
glossary = {
"variable": "A named storage location in memory that stores data.",
"function": "A block of reusable code that performs a specific task.",
    "loop": "A control flow statement for executing code repeatedly.",
    "list": "A data structure that holds an ordered collection of items.",
      "dictionary": "A data structure that holds key-value pairs."
}
for term,definition in glossary.items():
    print(f"{term.title()}:")
    print(definition)

print("-------------------------------------------------------------------------------")
"""
6-7. People: Start with the program you wrote for Exercise 6-1.
 Make two new dictionaries representing different people, 
 and store all three dictionaries in a list called people. Loop through your list of people.
 As you loop through the list, print everything you know about each person.
"""
people:list=[]
persona = {
    "nome": "Andrea",
    "cognome": "Bardi",
    "età": 20,
    "città": "Roma"
}

persona2 = {
    "nome": "Damiano",
    "cognome": "Libberati",
    "età": 20,
    "città": "Svizzera"
}
persona3 = {
    "nome": "Claudia",
    "cognome": "Marsella",
    "età": 47,
    "città": "Roma"
}
people.append(persona)
people.append(persona2)
people.append(persona3)

for i in people:
    print("nome:",i["nome"])
    print("cognome:",i["cognome"])
    print("età:",i["età"])
    print("città:",i["città"])
    

print("-------------------------------------------------------------------------------")
"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. 
"""



Animali_domestici:list[str]=[]

pets1:dict={"Animale":"Gatto","padrone":"Damiano"}
pets2:dict={"Animale":"Cane","padrone":"Andrea"}
pets3:dict={"Animale":"Pesce Rosso","padrone":"Giovanna"}
pets4:dict={"Animale":"Serpente","padrone":"Marco"}

Animali_domestici.append(pets1)
Animali_domestici.append(pets2)
Animali_domestici.append(pets3)
Animali_domestici.append(pets4)

for i in Animali_domestici:
    print("Animale:",i["Animale"])
    print("padrone:",i["padrone"])

print("------------------------------------------------------------")
"""
6-9. Favorite Places: Make a dictionary called favorite_places.
 Think of three names to use as keys in the dictionary,
   and store one to three favorite places for each person.
     To make this exercise a bit more interesting, 
     ask some friends to name a few of their favorite places.
 Loop through the dictionary, and print each person’s name and their favorite places.
"""
# Dictionary of favorite places
favorite_places = {
    "Andrea": ["Canada", "Jappan"],
    "Giovanni": ["Domodossola", "Matera"],
    "Charlie": ["London"]
}

# Loop through the dictionary and print each person's name and their favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print("- " + place)
print("--------------------------------------------------------------------")
"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each 
person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
"""
favorite_number:dict={"Andrea":[27,72],"Giovanni":[47,44],"Gaia":[3,501],"Frank":[8,10],"Daniele":[9,23]}

for name,number in favorite_number.items():

    print(f"Il numero preferito di {name} è {number}.")
print("--------------------------------------------------------------------")
"""
6-11. Cities: Make a dictionary called cities.
Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in,
its approximate population, and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact.
Print the name of each city and all of the information you have stored about it.
"""

# Dictionary of cities
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": 37300000,
        "fact": "Tokyo is the largest metropolitan area in the world."
    },
    "New York": {
        "country": "United States",
        "population": 19300000,
        "fact": "New York City is known as 'The Big Apple'."
    },
    "London": {
        "country": "United Kingdom",
        "population": 8900000,
        "fact": "London is the capital city of England and the United Kingdom."
    }
}

# Print information about each city
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
print("--------------------------------------------------------------")
"""
6-12. Extensions: We’re now working with examples that are complex enough that
they can be extended in any number of ways. Use one of the example programs from this chapter,
and extend it by adding new keys and values,
changing the context of the program, or improving the formatting of the output
"""
# Lista degli invitati iniziale
lista_invitati = ["Andrea", "Damiano", "Giovanni"]

# Stampa la lista degli invitati
print("Lista degli invitati iniziale:")
for nome in lista_invitati:
    print(f"Vorrei invitarti a cena, {nome}.")

# Simulazione di una persona che non può essere invitata
nome_rimosso = "Damiano"
print(f"\nScusa, {nome_rimosso} non può venire a cena.\n")

# Sostituire l'invitato con uno nuovo
nuovo_invitato = "Chiara"
lista_invitati[lista_invitati.index(nome_rimosso)] = nuovo_invitato

# Stampa un nuovo messaggio con la lista aggiornata degli invitati
print("Lista degli invitati aggiornata:")
for nome in lista_invitati:
    print(f"Vorrei invitarti a cena, {nome}.")

# Estensione del programma: Aggiunta di informazioni sugli invitati
informazioni_invitati = {
    "Andrea": {"età": 30, "professione": "studente"},
    "Giovanni": {"età": 25, "professione": "studente"},
    "Chiara": {"età": 28, "professione": "avvocato"}
}

# Stampa delle informazioni aggiuntive sugli invitati
print("\nInformazioni aggiuntive sugli invitati:")
for nome, info in informazioni_invitati.items():
    print(f"{nome}:")
    print(f"    Età: {info['età']}")
    print(f"    Professione: {info['professione']}")
