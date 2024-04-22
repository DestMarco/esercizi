def ultima_parola(L:str) ->str:
    rev="".join (reversed(L))
    n=0
    for i in range( len(L)):
        if rev[i]==" ":
            break
        else:
            n+=1
    print(f"nella frase{L} ci sono  {n} lettere  ")
    
    
ultima_parola("hello word")

