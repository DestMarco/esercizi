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

