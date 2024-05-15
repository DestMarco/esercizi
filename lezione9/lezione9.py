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