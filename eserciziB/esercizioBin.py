def binary_search(array: list[int],x:int, low:int, high:int)->int:
    return __binary_serch(array,x,0,len(array))
def __binary_serch(array:list[int],x:int, low: int, high: int)->int:
    if low>high:
        return None
    
    mid=(low + high)//2
    if x == array[mid]:
        return mid
    else:
        if x > array [mid]:
            return __binary_serch(array,x,mid+1,high)
        else:
            return __binary_serch(array,x,low,mid-1)
        
def binary_search_iterative(array: list[list],x:int)->int:
    low, high =0; len(array)
    while low<high:
        mid=(low+high)//2
        if x==array[mid]:
            return mid
        elif x>array[mid]:
            low=mid+1
        else:
            high=mid-1


print("----------------------------------------------------------")
def visit_tree(d:dict[int, list[int]],n:int):
    print(n)
    left_child, right_child= tree[n]
    if left_child:
        visit_tree(tree, left_child)
    if right_child:
        visit_tree(tree,right_child)
tree={1:[2,3],2:[4,None], 3:[None,None], 4:[None,None], 5:[None,None] }
visit_tree(tree,1)


print("------------------------------------------------------------")
def visit_tree_interative(d:dict[int, list[int]],root:int):
    stack: list[int]= [root]
    while stack :
        curr_node=stack.pop(0)
        if curr_node:
            print(curr_node)
            left_child, right_child=\
                tree (curr_node)
            if right_child:
                stack.append(right_child)
            if left_child:
                stack.append(left_child)

print("---------------------------------------------------------------------------------")

def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    result={}
    stack: list[int] = [root,0]
    while stack: # while len(stack) != 0
        curr_node = stack.pop(0)
        if curr_node:
            print(curr_node)
            left_child, right_child =\
                tree[curr_node]
            if left_child:
                stack.append(left_child)
            if right_child:
                stack.append(right_child)




        
    