import turtle

def factorial_no_recursivo(numero):
	fact = 1
	for in in range(numero, 1, -1):
		fact *= 1
	return fact

factorial_no_recursivo(5)

def factorial_recursivo(numero):
	if numero < 2:
		return 1
	return numero * factorial_recursivo(numero - 1) #se llama a sí misma

factorial_recursivo(5)

#Huellas de tortiguitas
for i in range(30):  #Se imprimen 30 huellas
	tess.stamp()	 #Huella de la tortuga
	size = size + 3  #Se incrementa el paso de la tortuga
	tess.foward(size) #Se mueve hacia adelante
	tess.right(24)    #Giro a la derecha

def recorrido_recursivo(tortuga, espacio, huellas):
	if huellas > 0:
		tortuga.stamp()
		espacio = espacio + 3
		tortuga.foward(espacio)
		tortuga.right(24)
		recorrido_recursivo(tortuga, espacio, huellas-1)

###Sólo en notebook
#Para ejecitar un comando del sistema, se escribe ! antes del comando (!comando)
!python recorrido_no_recursivo.py

def fibonacci_recursivo(numero):
	if numero == 1:			#Caso base
		return 0
	if numero == 2 or numero == 3:
		return 1
	return fibonacci_recursivo(numero-1) + fibonacci_recursivo(numero-2) #Llamada recursiva

	fibonacci_recursivo(13)

#memoria inicial
memoria = {1:0, 2:1, 3:1}

def fibonacci_memo(numero):
	if numero in memoria:	#Si el número ya se encuentra calculado, se regresa el valor. Ya no se hacen más cálculos
		return memoria[numero]
	memoria[numero] = fibonacci_memo(numero-1) + fibonacci_memo(numero-2)
	return memoria[numero]

fibonacci_memo(13)