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


