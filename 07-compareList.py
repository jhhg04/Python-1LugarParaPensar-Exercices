"""
7- Definir una función superposicion() que tome dos listas y devuelva True 
si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado.
"""
def superposicion(lista1,lista2):
    for elem in lista1:
        for elem2 in lista2:
            if elem == elem2:
                return True
    
    return False
    """
    manera elegante
    for elem in lista1:
        if elem in lista2:
            return True
    
    return False
    """
    
print('Superposicion:')
print(superposicion([1,2,3],[7,4,5]))
print(superposicion([1,2,5],[7,4,5]))