def bubble_sort(x:list[float]):
    for _ in range(len(x)):
        for j in range(len(x)-1):
            if x[j]>x[j+1]:
                temp:float=x[j+1]
                x[j+1]=x[j]
                x[j]= temp

a = [8,2,3,7,5]
bubble_sort(a)
print(a)

print("_---------------------------------------------------------------------------------------")
"""
Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
      # Step 1: Collect values from the linked list
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Step 2: Return the collected values in reversed order
    return values[::-1]

print ("----------------------------------------------------------------------------------------")

"""
Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa,
in genere utilizzando tutte le lettere originali esattamente una volta.
"""
from collections import Counter

def anagram(s: str, t: str) -> bool:
    # Se le lunghezze delle stringhe sono diverse, non possono essere anagrammi
    if len(s) != len(t):
        return False
    
    # Conta i caratteri di entrambe le stringhe
    return Counter(s) == Counter(t)



print("-------------------------------------------------------------------------")
"""
Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.

La lista di interi è formata così:

    L'elemento in posizione 0 corrisponde alla radice
    Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
    Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
    Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che corrisponde a quell'indice è una foglia.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(tree: list[int], index: int) -> TreeNode:
    if index >= len(tree) or tree[index] is None:
        return None
    node = TreeNode(val=tree[index])
    node.left = build_tree(tree, 2 * index + 1)
    node.right = build_tree(tree, 2 * index + 2)
    return node

def is_symmetric(left: TreeNode, right: TreeNode) -> bool:
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val) and is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)

def symmetric(tree: list[int]) -> bool:
    if not tree:
        return True
    root = build_tree(tree, 0)
    return is_symmetric(root.left, root.right)


print("----------------------------------------------------------------------------------------------------")









class Account:
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance = 0.0
    
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
    
    def get_balance(self) -> float:
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id: str) -> Account:
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists") 
        account = Account(account_id)
        self.accounts[account_id] = account
        return account
    
    def deposit(self, account_id: str, amount: float) -> bool:
        if account_id not in self.accounts:
         raise ValueError("Account not found") 
        self.accounts[account_id].deposit(amount)
        return True
        
    def get_balance(self, account_id: str) -> float:
        if account_id not in self.accounts:
            raise ValueError("Account not found") 
        



def valid_sudoku(board: list[list[str]]) -> bool:
    rows = []
    for _ in range(9):
        rows.append(set())
    colums=[]
    for _ in range(9):
        colums.append(set())
    boxe=[]
    for _ in range(9):
        boxe.append(set())
    for i in range (9):
        for j in range (9):
            n=board[i][j]
            box_index = (i//3)*3+(j//3)
            if n in rows[i]:
                return False
            if n in colums[j]:
                return False
            if n in boxe [box_index]:
                return False
            
            if n != '.':
                rows[i].add(n)
                colums[j].add(n)
                boxe[box_index].add(n)
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))

print("---------------------------------------------------------------------------------------")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def revers(self,head:ListNode):
    reversed_list:list[int]=[]
    queque:list[int]=[head]
    while queque:
        curr_node=queque.pop(0)
        if curr_node:
            reversed_list.append(curr_node.val)
            queque.append(curr_node.next)
    return reverse_list[::-1]


    pass
head=ListNode(val=0, 
              next=ListNode(val=1,
                            next=ListNode(val=5,
                                          next=ListNode(val=6))))
print(revers(head))

print("--------------------------------------------------------------------------------------")


class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    queue: list[ListNode] = [head]
    
    while queue:
        curr_node = queue.pop()
        if curr_node:
            reversed_list.append(curr_node.val)
            queue.append(curr_node.next)
    return reversed_list[::-1]

def reverse_recursive(head: ListNode) -> list[int]:
    reversed_list: list[int] = []
    _reverse(head, reversed_list)
    return reversed_list[::-1]

def _reverse(curr_node: ListNode, reversed_list: list[int]):
    if curr_node:
        reversed_list.append(curr_node.val)
        _reverse(curr_node.next, reversed_list)
        

head = ListNode(val=0, 
                next=ListNode(val=1, 
                              next=ListNode(val=5, 
                                            next=ListNode(val=6))))
print(reverse(head))