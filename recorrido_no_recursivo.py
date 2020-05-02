import turtle

wn = turtle.Screen()
wn.bgcolor("antiquewhite")
tortu = turtle.Turtle()
tortu.shape("turtle")
tortu.color("blueviolet")

tortu.penup()
size = 20

for i in range(30):
	tortu.stamp()
	size = size + 3
	tortu.forward(size)
	tortu.right(24)
    
wn.mainloop()