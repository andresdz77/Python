#PROBADO CON ANACONDA (PYTHON) 2.7

from cifrados import cicesar,decesar, cihill, dehill
from random import randint
#DEFINICION VARIABLE PARA QUE EL PRIMER NUMERO SEA RANDOM
i = randint(0,4) #RANGO DE LOS NUMEROS ALEATORIOS

#CONDICION BUCLE INFINIT0 PARA QUE TODOS TENGAN MISMA POSIBILIDAD
while i < 11:
	#CONDICION BUCLE INFINIT0 CON PROBABILIDAD PARA HILL
	while i < 5:
		#INTRODUCE MENSAJE
		mensaje = raw_input("introducir frase o palabra: ")
		#ENCRYPTA MENSAJE
		encryptado= cihill(mensaje)
		print(encryptado)
		#DESENCRYPTA MENSAJE
		desencryptado= dehill(encryptado)
		print(desencryptado)
		#CREA NUMERO ALEATORIO
		i = randint(0,4)
		print(i)
	#CONDICION BUCLE INFINIT0 CON PROBABILIDAD PARA CESAR
	while i >= 5:
		mensaje = raw_input("introducir frase o palabra: ")
		#ENCRYPTA MENSAJE
		encryptado = cicesar(mensaje)
		print(encryptado)
		#DESENCRYPTA MENSAJE
		desencryptado = decesar(encryptado)
		print(desencryptado)
		#CREA NUMERO ALEATORIO
		i = randint(0,10)
		print(i)
