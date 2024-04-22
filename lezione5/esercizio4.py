def majority_element(nums:list[int])->int:
    #creo il contatore
    # creo la variabbile del maggiore 
    
    #se il conteggio è zero, impostiamo il maggiore a num
    for i in range(len(nums)):
        # verifico se lelemento trovato comapare più di n/2 volte e se compagliono due elementi mi stapa none 
        if nums.count(i)> len(nums)/2 :
            return i
    return None 

print(majority_element(nums=[3,3,3,3,3,3,4,4,4,4,4]))
         




        


    