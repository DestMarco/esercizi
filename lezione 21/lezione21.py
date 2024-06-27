"""def generatore ():

    yield'A'
    yield'B'
    yield'C'

prova_generatore=generatore()


print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))
"""
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
    return raggio * raggio *3.14