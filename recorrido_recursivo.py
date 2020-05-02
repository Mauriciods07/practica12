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
ap.add_argument('--scolor', help="color de fondo del programa")
ap.add_argument('--tcolor', help="color de la tortuga")

#Crear las variables que crearán a la tortuga y asignarán valor a las huellas y a los espacios
args = vars(ap.parse_args())
scolor = args["scolor"]
tcolor = args["tcolor"]
huellas = int(args["huellas"])
espacio = int(args["espacio"])

#crear la tortuga
wn = turtle.Screen()
if scolor is None:
    #Color predeterminado de la pantalla si no se introdujo alguno en el cuerpo del código
    wn.bgcolor("lightgreen")
else:
    wn.bgcolor(scolor)
tort = turtle.Turtle()
tort.shape("turtle")
if tcolor is None:
    #Color predeterminado de la tortuga si no se introdujo alguno en el cuerpo del código
    tort.color("blue")
else:
    tort.color(tcolor)
tort.penup()

#Llamar a la función
recorrido_recursivo(tort, espacio, huellas)