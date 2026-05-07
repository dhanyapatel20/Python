import turtle
turtle.Screen().bgcolor("red" )
turtle.Screen().setup(100,300)
p=turtle.Turtle()

n=5
l=70
a=360/n
for i in range(n):
    p.forward(l)
    p.right (a)
turtle.done()
