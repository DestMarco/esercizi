





def mergesort(input_list):

    if len(input_list)==1:
        return input_list
    
    mid_point=len(input_list)//2

    mergesort(input_list=input_list[:mid_point])
    mergesort(input_list=input_list[:mid_point])

if __name__=="__main__":

    input_list:list[int]=(0,1,2,4,5,6,7)

    mergesort(input_list=input_list)