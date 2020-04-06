import turtle

#Just a Simple Square
turtle = turtle.Turtle()

def square_1():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

def square_2():
  square_1()
  turtle.forward(0)
  square_1()

square_2()