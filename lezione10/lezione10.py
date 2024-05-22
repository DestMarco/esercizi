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
import getpass


print("esempio")
username = input ("Enter Username")
print("Username is:" + username)

if username != "Marco":
    print("Username non valido")
else:
    password = getpass.getpass("Enter Password: ")
    print("Password entered")

    if password != "Marcolino71":
        print("Password non valida")
    else:
        print("Username e password validi")
        


