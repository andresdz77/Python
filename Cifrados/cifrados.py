#PROBADO CON ANACONDA (PYTHON) 2.7

from sympy.solvers import solve
from sympy import Symbol
import numpy as np
from itertools import chain
# MATRIZ LLAVE
a = np.matrix('17 17 12; 9 4 5; 17 6 6')
adja = np.matrix('250 226 37; 31 154 23; 242 187 171') #ADJUNTA

#----------------------CIFRADO CESAR------------------------------------#

#-----------------------CIFRADO-----------------------------------------#


def cicesar(mensaje):
    texto_cifrado = ""
    for caracter in mensaje:
        texto_cifrado = texto_cifrado + chr(ord(caracter) + 3)
    return texto_cifrado
#----------------------DECIFRADO-----------------------------------------#


def decesar(mensaje):
    texto_decifrado = ""
    for caracter in mensaje:
        texto_decifrado = texto_decifrado + chr(ord(caracter) - 3)
    return texto_decifrado

#----------------------CIFRADO HILL------------------------------------#


def letter(n):
    return chr(n)
#-----------------------CIFRADO-----------------------------------------#


def cihill(mensaje):
        # Condicion para que cualquier mensaje pueda ser transformado en matriz
    r = len(mensaje)
    while r % 3 != 0:
        r = r + 1
        mensaje = mensaje + " "
    c = list(mensaje)
    # Matriz de numeros
    w = [ord(i) for i in mensaje]
    y = np.array(w).reshape(3, r / 3)
    # MULTIPLICACION DE MATRIZ DE NUMEROS X MATRIZ LLAVE
    z = (a * y) % 256
    zz = z.tolist()
    letters = [[letter(n) for n in row] for row in zz]
    final = ''.join([''.join(row) for row in letters])
    return final

#-----------------------DECIFRADO-----------------------------------------#


def dehill(mensaje):
    c = list(mensaje)
    # Matriz de numeros
    w = [(ord(i)) for i in mensaje]
    z = np.array(w).reshape(3, len(mensaje) / 3)
    # DETERMINANTE MATRIZ LLAVE
    p = np.linalg.det(a) % 256
    # LLAVE A LA -1
    pp = (p * adja) % 256
    # INVESTIGAR SACAR EL ADJUNTO CON MODULO
    s = (pp * z) % 256
    ss = s.tolist()
    sss = [[int(round(i)) for i in row] for row in ss]
    lettersx = [[letter(n) for n in row] for row in sss]
    finalx = ''.join([''.join(row) for row in lettersx])
    return finalx
