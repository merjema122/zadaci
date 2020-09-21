def max_min(lista):
 max=lista[0]
 min=lista[0]
 for x in lista:
  if x>max:
    max=x
  elif (x<min):
     min=x
 return max, min

print(max_min([0,1,2,3,4,50,5]))
    