import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.bgcolor("skyblue")

# Create a turtle
t = turtle.Turtle()

# Draw the castle walls
color("gray")
begin_fill()
for _ in range(4):
    forward(100)
    left(90)
end_fill()

# Draw the roof
penup()
goto(-50, 0)
pendown()
color("red")
begin_fill()
for _ in range(3):
    forward(200)
    left(120)
end_fill()

# Draw the door
penup()
goto(25, -100)
pendown()
color("brown")
begin_fill()
for _ in range(2):
    forward(50)
    left(90)
    forward(100)
    left(90)
end_fill()

# Draw windows
def draw_window(x, y):
    penup()
    goto(x, y)
    pendown()
    color("cyan")
    begin_fill()
    for _ in range(4):
        forward(30)
        left(90)
    end_fill()

draw_window(-30, 0)
draw_window(40, 0)

# Hide the turtle
hideturtle()

# Keep the window open
screen.mainloop()











     



exitonclick()
