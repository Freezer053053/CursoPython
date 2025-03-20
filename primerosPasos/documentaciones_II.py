import math

def raizCuadrada(listaNumeros):
    """
    La función devuelve una lista con la 
    raíz cuadrada de los elementos numéricos
    pasados por parámetros en otra lista

    >>> lista=[]
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4, -9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """
    return [math.sqrt(n) for n in listaNumeros]

#print (raizCuadrada([9, 16, 25, 36]))

import doctest
doctest.testmod()

lista_numeros = [9, 25, 121]

print(raizCuadrada(lista_numeros))
