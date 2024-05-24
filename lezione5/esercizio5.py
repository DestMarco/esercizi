"""
data una lista di interi, spostare gli zerialla fine di 
questa lista mantenendo l'ordine origginale 
dei nueri che non sono zeri
"""
def move_zeroes(nums:list[int]):
    zero_index=0
    for i in nums:
        if i !=0:
            nums[zero_index]=i
            zero_index +=1
    for i in range(zero_index, len(nums)):
        nums[i]=0
    return nums 
print(move_zeroes(nums=[1,0,3,0,4,0,8,0,10,0,0,0,0,0,0,1,9]))

print("----------------------------------------------------------------------")


def rotate_left(lst,k):
    if not lst:
        return[]
    if k==0:
        return lst
    k = k % len(lst)
    return lst[k:] + lst[:k]

print (rotate_left([1,2,3,4,5],2))


def print_seq():
    # Sequenza a)
    print("Sequenza a):")
    for i in range(1, 8):
        print(i)
  
    print("\nSequenza b):")
    # Sequenza b)
    for i in range(3, 24, 5):
        print(i)
        
    print("\nSequenza c):")
    # Sequenza c)
    for i in range(20, -12, -6):
        print(i)
        
    print("\nSequenza d):")
    # Sequenza d)
    for i in range(19, 52, 8):
        print(i)
        break 
# Esegui la funzione per stampare le sequenze
print_seq()