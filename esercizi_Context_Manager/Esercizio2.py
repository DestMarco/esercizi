"""Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1"""


import time 

class Time:
    def __init__(self):
        self.start_time=None

    def __enter__ (self):
        self.start_time=Time.time()
        return self
    
    def __exit__ (self, exc_type, exc_val, exc_tb):
        end_time=Time.time()
        el_time=end_time-self.start_time
        print(f"time elapsed:{el_time:.5f}second")
        if exc_type is not None:
            print(f"Exception: {exc_type}, value : {exc_val}, Traceback{exc_tb}")
        return False 
with Time():
    time.sleep(1)
