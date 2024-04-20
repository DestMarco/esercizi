#definisco e creo una funzione 
def subtract (a:int,b:int):
# creo una variabbile che contiene la sottrazione tra le due variabbili
    z:int=a-b
#restiusce il valore z fuori dalla funzione 
    return z
#richiamo la funzione 
print(subtract(18,5))

print("---------------------------------------------------------------------")


def check_value(n:int):
    if n==5:
        print(f"{n} è uguale a 5")
    elif n>5:
        print(f"{n} è maggiore a 5")
    elif n<5:
        print(f"{n} è minore a 5")
    

check_value(4)

print("--------------------------------------------------------------")


def check_lenght(n:str):
    if len(n)==10:
        print(f"la stringa {n} contine 10 caratteri")
    elif len(n)>10:
        print(f"la stringa {n} contine più di 10 caratteri")
    elif len(n)<10:
        print(f"la stringa {n} contine meno di 10 caratteri")
    

check_lenght("hello word")

print("-------------------------------------------------------------")

def print_numbers(L:list):
 
    for i in L:
          print(i)

L:list=[1,2,3,4,5]
print_numbers(L)

print("-----------------------------------------------------------")


def print_numbers(L:list):
 
    for i in L:
        if i==5:
            print(f"{i} è uguale a 5")
        elif i>5:
            print(f"{i} è maggiore rispetto 5")
        elif i<5:
            print(f"{i} è minore rispetto 5")
          

L:list=[1,2,3,4,5,6,6,7,8,9,10]
print_numbers(L)


print("-----------------------------------------------------------")

"""
Write a function add_one(). It takes an integer as argument. The function adds 1 to
the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.
"""

def add_one(N:int):
     
     return N+1
def add_one_to_list(lis:list):
    new_list:list=[]
    for N in lis:
        new_list.append(add_one(N))
    print(new_list)
    
my_list=[1,2,3,4,5,6,7,8]
add_one_to_list(my_list)
    
 





    




