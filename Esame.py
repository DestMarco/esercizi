"""Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
For example:

Test	Result
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
b
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))
None
"""


def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key in dizionario:
        if dizionario[key]==valore:
            return key


"""Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51
For example:

Test	Result
print_seq()
Sequenza a):
1
2
3
4
5
6
7

Sequenza b):
3
8
13
18
23

Sequenza c):
20
14
8
2
-4
-10

Sequenza d):
19
27
35
43
51
"""


def print_seq(): 
    
    print("Sequenza a):")
    for a in range(1,8) :
        print(a)
    print()
    print("Sequenza b):")
    for b in range (3,28,5):
        print(b)
    print()
    print("Sequenza c):")
    for i in range (20,-16,-6):
        print(i)
    print()
    print("Sequenza d):")
    for d in range (19,59,8):
        print(d)
    print()
    
    return



"""Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
For example:

Test	Result
print(frequency_dict(['mela', 'banana', 'mela']))
{'mela': 2, 'banana': 1}
"""


def frequency_dict(elements: list) -> dict:

    freq_dict = {}
    for item in elements:
        if item in freq_dict:
            freq_dict[item] +=1
        else:
            freq_dict[item]=1
    return freq_dict
    
    
"""Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
For example:

Test	Result
print(transform(4))
2
print(transform(-10))
-5"""



def transform(x):
    if x % 2 == 0:
        return x // 2  
    else:
        return x * 3 - 1  

"""
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
For example:

Test	Result
print(classifica_numeri([1, 2, 3, 4, 5, 6])) 
{'pari': [2, 4, 6], 'dispari': [1, 3, 5]}
print(classifica_numeri([]))
{'pari': [], 'dispari': []}
"""


def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dict={"pari":[],"dispari":[]}
    for n in lista:
        if n % 2==0:
            dict["pari"].append(n)
        else:
            dict["dispari"].append(n)
    return dict
    

"""Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
For example:

Test	Result
print(sum_above_threshold([15, 5, 25], 20))
25
"""


def sum_above_threshold(numbers: list[int],threshold:int)->int:
    sum=0
    for i in numbers:
        if i > threshold:
            sum += i
    return sum




"""Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

For example:

Test	Result
print(merge_dictionaries({'x': 5}, {'x': -5}))
{'x': 0}

    """

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    merge_dict=dict1.copy()
    
    for key, value in dict2.items():
        if key in merge_dict:
            merge_dict[key] += value
        else:
            merge_dict[key] = value
            
    return merge_dict






"""Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
For example:

Test	Result
print(check_combination(True, False, True))
Operazione permessa
print(check_combination(False, True, False))
Operazione negata"""





def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or (conditionB and conditionC):
        return "Operazione permessa"
    else:
        return "Operazione negata"




"""Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".
For example:

Test	Result
print(check_access("admin", "12345", True))
Accesso consentito
print(check_access("admin", "54321", True))
Accesso negato"""



def check_access(username, password, account_active):
    if username == "admin" and password == "12345" and account_active:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    


"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
For example:

Test	Result
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
{'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) """



def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:

    scontati = {}
    for prodotto, prezzo in prodotti.items():
        if prezzo > 20:
            scontati[prodotto] = round(prezzo * 0.9, 2)  # Applica sconto del 10% e arrotonda a 2 decimali
    return scontati
