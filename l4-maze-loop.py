import turtle

screen = turtle.Screen()
agnes = turtle.Turtle()
agnes.speed(10)

length = 5
for _ in range(0, 100):
    agnes.forward(length)
    agnes.left(90)
    length += 5


screen.exitonclick()