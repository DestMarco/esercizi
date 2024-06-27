"""def generatore ():

    yield'A'
    yield'B'
    yield'C'

prova_generatore=generatore()


print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))
""""""
from contextlib import contextmanager

@contextmanager
def context_manager_decorator():
    import time

    start_line:float=time.time()

    yield

    end_time:float=time.time()
    elapsed_time:float=end_time - start_line

    print(f"{elapsed_time}")

@context_manager_decorator
def area_cerchio(raggio:float):
    return raggio * raggio *3.14"""
"""
import sys

a=[]

b=a

print(sys.getrefcount(a))

"""

print("------------------------------------------------------------------------")
import time
def thread_fuction(name):
    print(f"{name} Time-{time.time()}")
    time.sleep(2)
    print(f"{name} Time-{time.time()}")

import threading

for i in range(3):
    x= threading.Thread(target=thread_fuction, args=(1,))
    

print (f"prima di thread")
x.start()
print (f" thread partito")

print (f" thread finitoo????")
