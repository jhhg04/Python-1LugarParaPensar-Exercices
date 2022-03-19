"""
6 - Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""
def inversa(cadena):
  longitud = -(len(cadena)-1)
  nueva_cadena = str()
  for n in range(longitud,1):
    n = abs(n)
    nueva_cadena += cadena[n]
  return nueva_cadena

def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        return True
    
print(es_palindromo('arenera'))