"""
Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e 
viceversa a seconda del parametro to_fahrenheit.
 Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
"""
def convert_temperature(temperature: int, to_fahrenheit=True) -> float:
    if to_fahrenheit:
        temperature: float = temperature * 9/5 + 32
        return temperature
    else:
        temperature: float= (temperature -32) / 1.8
        return temperature

print (convert_temperature(20))
print (convert_temperature(70, to_fahrenheit=False))

"""
Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". 
Un numero magico è definito come un numero che contiene il numero 7.
"""
def is_magic_number(num: int) -> bool:
    n_t=str(num)
    if "7" in n_t :
      return True
    else:
      return False


print(is_magic_number(70)) 


"""

Il codice dovrebbe stampare i numeri all'interno di una lista.

TROVA L'ERRORE E CORREGGI IL CODICE

"""

numbers: list[int] = [1, 2, 3, 4, 5]

for i in numbers:
    print('Number:', i)

print("---------------------------------------------")

"""
La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.

Trova l'errore e correggi il codice affinché soddisfi i casi di test.

For example:
"""


def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return sum(numbers) + len(numbers)
    else:
        return sum(numbers) / len(numbers)
    


print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))

print(calculate_average([10, 20, 30]))

"""
Scrivi una funzione che ritorna il valore massimo,
 minimo e la media di una lista di numeri interi.
"""

def list_statistics(numbers: list[int]) -> int :
        
        max_value:int=max(numbers)
        min_value:int=min(numbers)
        avg:float=sum(numbers) / len (numbers)

        return max_value, min_value, avg
    
print(list_statistics(numbers=[1,10,9,7,4]))



"""
Scrivi una funzione che accetti tre parametri: username, password
 e status di attivazione dell'account (attivo/non attivo).
   L'accesso è consentito solo se il nome utente è "admin",
     la password corrisponde a "12345" e l'account è attivo.
 La funzione ritorna "Accesso consentito" oppure "Accesso negato".
"""
def check_access(username: str, password: str, is_active: bool) -> str:
    if username ==  "admin" and password == "12345" and is_active:
       return "Accesso consentito"
    else:
        return"Accesso negato"
print(check_access(username="admin",password="12345",is_active=True))

"""
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate,
 cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
"""
       
def check_parentheses(expression: str) -> bool:
    l1:list=[]
    l2:list=[]
    for i in expression:
        if len(l2)>len(l1):
            return False
        if i == ')':
            l2.append(i)
        elif i == '(':
            l1.append(i)
        else:
             continue
    return True

print(check_parentheses("()()"))

print(check_parentheses("(()))("))

print(check_parentheses("((()))"))

print(check_parentheses(")("))

print(check_parentheses("(())"))
    
"""
Scrivi una funzione che conta e ritorna quante volte un elemento appare
isolato in una lista di numeri interi. Un elemento è
considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
"""
def count_isolated(num:int) -> int:
    c=0
    for i in range(len(num)):
        if i == 0 and num[i] !=num[i+1]:
            c+=1
        # i== len (num)-1 (controlla se i è l'ultimo indice della lista)
        elif i == len(num)-1 and num[i] != num[i-1]:
            c+=1
        elif num[i] != num[i-1] and num[i] != num[i+1]:

            c+=1
    return c

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 1, 2, 2, 3, 4, 4]))


"""
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere,
ritorni un nuovo insieme senza i numeri specificati nella lista.
"""

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    return original_set - set(elements_to_remove)


"""
Scrivi una funzione che unisce due dizionari.
 Se una chiave è presente in entrambi, somma i loro valori.
"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3=dict1|dict2
    for i in dict3: 
        if i in dict1 and i in dict2:
            dict3[i]=dict1[i]+dict2[i]

    return dict3
print(merge_dictionaries({'x': 5}, {'x': -5}))