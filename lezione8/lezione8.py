"""
class Animal:
    def __init__(self,specie:str,età:int,nome:str):
        self.specie=specie
        self.età=età
        self.nome=nome
    def __str__(self) -> str:
        return f'{self.__class__.__name__}(name{self.nome},specie={self.specie}, eta={self.età})'
class Person(Animal):
    def __init__(self, età: int,surname:str, nome:str,cod_fiscale:str, specie="Homo Sapiens"):
        super().__init__(specie, età)
        self.nome=nome
        self.cod_fiscale=cod_fiscale
        self.surname=surname
    def __str__(self) -> str:
        return f"{self.nome.capitalize()}{self.surname.capitalize()}(cf={self.cod_fiscale})"\
            + f",age={self.età}"\
            + f",specie={self.specie}"

class Studente(Person):
    def __init__(self, età: int, surname:str ,nome: str, cod_fiscale: str, N_ma:str ,specie="Homo Sapience"):
        super().__init__(età, nome, cod_fiscale, specie)
        self.N_ma=N_ma    
    
class Gat(Animal):
    def __init__(self,  età: int,nome:str,specie="Felidae"):
        super().__init__(specie, età)
        self.nome=nome
    def __str__(self) -> str:
        return f"name={self.nome},eta={self.età}, specie={self.specie}"
class Rabit(Animal):
    def __init__(self, età: int,nome:str , specie="Leporidae"):
        super().__init__(specie, età)
        self.nome=nome
    def __str__(self) -> str:
        return f"nome={self.nome},age={self.età},specie={self.specie}"

P=Person(nome="lorenzo",surname="Maggi",cod_fiscale="bella",età=22,specie="Homo Sapiens")
a=Animal(nome="willi",specie="Balaen Balana",età=25)
print(P)
print(a)
c= Gat(nome="Garfield",età=15,specie="Felidae")
print(c)
"""
print("----------------------------------------------------------------------------------------------------------")
class Rooms:
    def __init__(self,id:str,floor:int,seats:int):
          self.id=id
          self.floor=floor
          self.seats=seats
    def get_floor(self):
         return self.floor
    def get_seats(self):
         return self.seats
    def get_id(self):
         return self.id
    def __str__(self) -> str:
         return f"Rooms=(id={self.id},floor={self.floor},seats={self.seats})"
        
class Bulding:
    def __init__(self,name:str,num_float:str,address:str,rooms:list=[Rooms]) -> None:
        self.name=name
        self.address=address
        self.num_float=num_float
        self.rooms:list [Rooms]=rooms
    def get_num_float(self):
         return self.num_float
    def get_rooms(self):
         return self.rooms
    def add_room(self,room:Rooms):
         if room not in self.rooms\
          and room.get_floor() <= self.get_num_float():
              self.rooms.append(room)
    def __str__(self):
            return f"{self.name.capitalize()}@{self.address}"
smi=Bulding(name="SMI",address="via sierra nevada à60",num_float=5)
smi.add_room(id="666",floor=3,seats=32)

print("---------------------------------------------------------------------------------")


"""
Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- push(x: int) -> None: Pushes element x to the top of the stack.
- pop() -> None Removes the element on the top of the stack and returns it.
- pop() -> None Returns the element on the top of the stack.
- empty() -> None Returns true if the stack is empty, false otherwise.
"""
print("--------------------------------------------------------------------")
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def size(self) -> int:
        return len(self.queue)


class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:

        while not self.queue1.is_empty():
            self.queue2.enqueue(self.queue1.dequeue())
        
        self.queue1.enqueue(x)
        
        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

    def pop(self) -> int:
        return self.queue1.dequeue()

    def top(self) -> int:
        return self.queue1.queue[0] if not self.queue1.is_empty() else None

    def empty(self) -> bool:
        return self.queue1.is_empty()
    
print("------------------------------------------------------")
print("Esercizi")
def longest_palindrome(s: str) -> int:
    length = 0
    odd_found = False
    

    for char in set(s):  
        count = s.count(char)
        length += count // 2 * 2  
        if count % 2 == 1:
            odd_found = True
    
    if odd_found:
        length += 1
    
    return length
print("-------------------------------------------------------------------------")

def is_valid_parenthesis(s: str) -> bool:
    l1:list=[]
    l2:list=[]
    for i in s:
        if len(l2)>len(l1):
            return False
        if i == ')]}':
            l2.append(i)
        elif i == '([{':
            l1.append(i)
        else:
             continue
    l3=l1+l2
    return True
print("---------------------------------------------------------------------------")
def merge(nums1, m, nums2, n):
    p1,p2 =m-1,n-1
    p=m+n-1
    while p1 >=0 and p2>=0:
        if nums1[p1]>nums2[p2]:
            nums1[p] = nums1[p1]
            p1-=1
        else:
            nums1[p]=nums2[p2]
            p2 -=1
        p -=1
    while p2 >=0:
        nums1[p] = nums2[p2]
        p2-=1
        p-=1
    return nums1
print("--------------------------------------------------------------------------------")

