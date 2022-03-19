"""
5- Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena):
  longitud = -(len(cadena)-1)
  nueva_cadena = str()
  for n in range(longitud,1):
    n = abs(n)
    nueva_cadena += cadena[n]
  return nueva_cadena

print(inversa('estoy probando'))