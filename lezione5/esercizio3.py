"""
dato un intero col_number, restituire il suo corrispondente titolo di colonna come ad esempio
compare su foglio Excel

esempio 1:
col_number =1 -> restiture "A"
"""

def convert_to_title(col_number:int)->int:
  result:str=""
  while col_number>0:
    r:int=(col_number-1)%26 #questo mi da il resto
    result=chr(r+ ord("A"))+result
    col_number=(col_number-1)//26
  return result

print(convert_to_title(10))



