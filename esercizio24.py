from multiprocessing import Process
import time

def bubblesort():
    from random import randint
    x=[randint(0,10000) for _ in range(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)]

    ho_fatto_swap:bool=True
    for i in range (len(x)):
        for j  in range (len(x)-i-1):
            if x [j] > x[j+1]:
                ho_fatto_swap=False
                tempo:int=x[j]
                x[j]=x[j+1]
                x[j+1]=tempo
        if ho_fatto_swap:
            break


       
def sleep():
    print(f"sono nella funzione")

    time.sleep(60)

    print(f"sono uscito dalla funzione")

if __name__=="__main__":
    tic: float= time.time()
    t1=Process (target=bubblesort)
    t2 = Process (target=bubblesort)
    t3=Process (target=bubblesort)
    t4 = Process (target=bubblesort)
    t5=Process (target=bubblesort)
    t6 = Process (target=bubblesort)
    t7=Process (target=bubblesort)
    t8 = Process (target=bubblesort)
    t9=Process (target=bubblesort)
    t10 = Process (target=bubblesort)
    t11=Process (target=bubblesort)
    t12= Process (target=bubblesort)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t12.start()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    toc:float=time.time()
    time_elapsed: float= toc-tic

    print(f"{time_elapsed=}")
