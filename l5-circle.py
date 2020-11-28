import turtle

screen = turtle.Screen()
agnes = turtle.Turtle()
agnes.speed(10)

radius = 5
for _ in range(0, 100):
    agnes.circle(radius)
    radius += 5


screen.exitonclick()