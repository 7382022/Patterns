import turtle


t = turtle.Turtle()

def draw_square():
    for _ in range(4):
        t.forward(-60)
        t.left(90)

t.penup()
t.goto(-250, 270)
t.pendown()
draw_square()

t.penup()
t.goto(250, 270)
t.pendown()
draw_square()

t.penup()
t.goto(-250, -250)
t.pendown()
draw_square()

t.penup()
t.goto(250, -250)
t.pendown()
draw_square()

t.penup()
t.goto(0, 0)
t.pendown()
draw_square()

t.penup()
t.goto(0, 30)
t.pendown()
draw_square()

t.penup()
t.goto(0, -30)
t.pendown()
draw_square()

t.penup()
t.goto(30, 0)
t.pendown()
draw_square()

t.penup()
t.goto(-30, 0)
t.pendown()
draw_square()

t.penup()
t.goto(-30, 30)
t.pendown()
draw_square()

t.penup()
t.goto(30, 30)
t.pendown()
draw_square()

t.penup()
t.goto(-30, -30)
t.pendown()
draw_square()

t.penup()
t.goto(30, -30)
t.pendown()
draw_square()



t.hideturtle()
turtle.done()

print("WHATCH UNTIL THE END IT IS NOT OVER")