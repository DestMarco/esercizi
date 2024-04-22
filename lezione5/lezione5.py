def is_palindromo(X):
    S:str=str(X)
    rev="".join(reversed(S))
    
    if S == rev:
      return True
    else:
       return False

print(is_palindromo(151))

