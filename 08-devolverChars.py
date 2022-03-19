"""
8- Definir una función generar_n_caracteres() que tome un entero n y 
devuelva el caracter multiplicado por n. Por ejemplo: 
generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
def generar_n_caracteres(caracter,n):
    string = caracter
    print(caracter * n)
    """
    for i in range(1,n):
        string += caracter
    
    print(string)
    """

generar_n_caracteres('abc',3)

