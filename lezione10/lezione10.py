"""
def is_symmetric(tree: list[int])-> bool:
    return are_mirrored(tree,1,2)

def are_mirrored(tree,left_index, right_index)-> bool:
    
    if left_index >= len(tree) and right_index >= len(tree):
        return True
    
    elif (left_index >= len(tree) and right_index < len(tree))\
          or (left_index < len(tree) and right_index >= len(tree)):
        return False
    
    if tree[left_index] != tree[right_index]:
        return False    
    
    left_of_left=2*left_index+1
    right_of_left=2*left_index+2
    left_of_right=2*right_index+1
    right_of_right=2*right_index+2

    is_symmetric_external:bool=are_mirrored(tree,left_of_left,right_of_right)
    is_symmetric_internal:bool=are_mirrored(tree,right_of_left,left_of_right)
    return is_symmetric_internal and is_symmetric_external

"""    
def rotate_left(lst,k):
    if not lst:
        return[]
    if k==0:
        return lst
    k=k%len(lst)
    return lst[k:]+lst[:k]
print(rotate_left([1,2,3,4,5],2))

print("-----------------------------------------------------------------------------")

def trasform(x:int)->int:
    if x % 2 ==0:
        return x/2
    else:
        return x * 3 -1
print(trasform(3))


print("--------------------------------------------------------------------------------------")

def calcola_stipendio(ore_lavorate:int) -> float:
    paga_oraria =10.0
    ore_normali =40
    if ore_lavorate <= ore_normali:
        stipendio_lordo=ore_lavorate *paga_oraria
    else:
        ore_extra=ore_lavorate-ore_normali
        stipendio_lordo=(ore_normali*paga_oraria)+(ore_extra * paga_oraria * 1.5)
    return stipendio_lordo
print("-----------------------------------------------------------------------------------------")

def integerPower(base:int,esponente:int):
    if esponente != 0:
        return base ** esponente
    
    

