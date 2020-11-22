import turtle

screen = turtle.getscreen()
agnes = turtle.Turtle()

agnes.penup()
agnes.goto(-400, 0)
agnes.pendown()
agnes.forward(800)
agnes.stamp()

agnes.penup()
agnes.goto(0, -300)
agnes.pendown()
agnes.left(90)
agnes.forward(600)
agnes.stamp()


screen.exitonclick()