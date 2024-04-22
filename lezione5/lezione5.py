def is_palindromo(X):
    S:str=str(X)
    rev="".join(reversed(S))
    return S==rev
"""  
    if S == rev:
      return True
    else:
       return False
"""
    

print(is_palindromo(151))

