"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

def funcion_max3(n1,n2,n3):
  if n1 > n2 and n1> n3:
    return n1
  elif n2 > n1 and n2 > n3:
    return n2
  else:
    return n3

print(funcion_max3(1,11,2))