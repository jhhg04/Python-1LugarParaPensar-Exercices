"""
3- Escribir una función que tome un carácter y devuelva True si es una vocal, 
de lo contrario devuelve False.
"""
def is_vocal(caracter):
    lista_vocales = ['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    else:
        return False

print(is_vocal('e'))