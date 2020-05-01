import turtle
import argparse

def recorrido_recursivo(tortuga, espacio, huellas):
	if huellas > 0:
		tortuga.stamp()
		espacio = espacio + 3
		tortuga.forward(espacio)
		tortuga.right(24)
		recorrido_recursivo(tortuga, espacio, huellas-1)

#Crear las referencias para poder pasar la información desde el cuerpo del programa
ap = argparse.ArgumentParser(conflict_handler='resolve')
ap.add_argument('--huellas', required=True, help="número de huellas")
ap.add_argument('--espacio', required=True, help="espacio de recorrido")
ap.add_argument('--scolor', required=True, help="color de fondo del programa")
ap.add_argument('--tcolor', required=True, help="color de la tortuga")

#Crear las variables que crearán a la tortuga y asignarán valor a las huellas y a los espacios
args = vars(ap.parse_args())
scolor = args["scolor"]
args = vars(ap.parse_args())
tcolor = args["tcolor"]
args = vars(ap.parse_args())
huellas = int(args["huellas"])
args = vars(ap.parse_args())
espacio = int(args["espacio"])

#crear la tortuga
wn = turtle.Screen()
wn.bgcolor(scolor)
tort = turtle.Turtle()
tort.shape("turtle")
tort.color(tcolor)
tort.penup()

#Llamar a la función
recorrido_recursivo(tort, espacio, huellas)