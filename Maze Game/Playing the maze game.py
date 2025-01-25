import random
import turtle
from tkinter import messagebox

while True:
    size = int(input("Enter the size of the maze"))
    if 2 < size < 46: break
    else: print("Invalid size !")
wn = turtle.Screen()
key = turtle.Turtle()
r = random.randint(1, size ** 2)
key_taken = False
key_x, key_y = - 140 + (r % size) * 15, 310 - ((r - (r % size)) / size) * 15
key.color("purple"), key.shapesize(0.5, 0.5), key.shape("circle"), key.penup(), key.goto(key_x, key_y)


def up():
    try:
        global key_taken
        p = int((((solve.xcor() + 140) / 15) + 1) + (((310 - solve.ycor()) / 15) * size))
        x_cor = solve.xcor()
        y_cor = solve.ycor()
        if walls[p][2] is False or walls[p - size][3] is False:
            y_cor += 15
            solve.sety(y_cor)
        if (x_cor, y_cor) == (key_x, key_y):
            key.hideturtle()
            key_taken = True
    except KeyError:
        messagebox.showwarning("Warning", "You are trying to break into forbidden grounds")


def down():
    global p, key_taken
    try:
        p = int((((solve.xcor() + 140) / 15) + 1) + (((310 - solve.ycor()) / 15) * size))
        x_cor = solve.xcor()
        y_cor = solve.ycor()
        if walls[p][3] is False or walls[p + size][2] is False:
            y_cor -= 15
            solve.sety(y_cor)
        if (x_cor, y_cor) == (key_x, key_y):
            key.hideturtle()
            key_taken = True
    except KeyError:
        if p < size ** 2:
            messagebox.showwarning("Warning", "You are trying to break into forbidden grounds")
        else:
            if key_taken:
                om.color("green")
                messagebox.showinfo("Congratulations", '''Wow!!! You have conquered the maze, you are a true path-finder''')
            else: messagebox.showwarning("Warning", "Get the key first !!!")


def right():
    global key_taken
    try:
        p = int((((solve.xcor() + 140) / 15) + 1) + (((310 - solve.ycor()) / 15) * size))
        x_cor = solve.xcor()
        y_cor = solve.ycor()
        if walls[p][1] is False or walls[p + 1][0] is False:
            x_cor += 15
            solve.setx(x_cor)
        if (x_cor, y_cor) == (key_x, key_y):
            key.hideturtle()
            key_taken = True
    except KeyError:
        if key_taken:
            om.color("green")
            messagebox.showinfo("Congratulations", '''Wow!!! You have conquered the maze, you are a true path-finder !!!''')
        else: messagebox.showwarning("Warning", "Get the key first !!!")


def left():
    try:
        global key_taken
        p = int((((solve.xcor() + 140) / 15) + 1) + (((310 - solve.ycor()) / 15) * size))
        x_cor = solve.xcor()
        y_cor = solve.ycor()
        if walls[p][0] is False or walls[p - 1][1] is False:
            x_cor -= 15
            solve.setx(x_cor)
        if (x_cor, y_cor) == (key_x, key_y):
            key.hideturtle()
            key_taken = True
    except KeyError:
        messagebox.showwarning("Warning", "You are trying to break into forbidden grounds")


wn.bgcolor("black"), wn.setup(800, 720), wn.tracer(0)
z = turtle.Turtle()
solve = turtle.Turtle()
z.penup(), z.pencolor("red"), z.goto(-500, 290), z.hideturtle(), z.write("MAZE", align="left", font=("courier", 50, "bold"))
om = turtle.Turtle()
x, y = -147, 332
om.pencolor("orange"), om.pensize(6), om.hideturtle(), om.speed(0)
for i in range(1, size + 1):
    x = -147
    y -= 15
    for j in range(1, size + 1):
        om.penup(), om.goto(x, y), om.pendown(), om.forward(15), om.right(90), om.forward(15), om.right(90), om.forward(15), om.right(90), om.forward(15), om.right(90)
        x += 15
om.penup(), om.goto(-155, 245), om.showturtle(), om.shape("square"), om.shapesize(0.5, 0.5, 0.5), om.color("red")
l1 = []
walls = {}
for i in range((size ** 2) + 1):
    l1.append(0)
    walls[i] = [True, True, True, True]
rashi = turtle.Turtle()
rashi.penup(), rashi.pensize(9), rashi.shape("square"), rashi.shapesize(0.5, 0.5, 0.5), rashi.goto(-140,310), rashi.pendown(), rashi.color("white"), rashi.pencolor("black")
neighbours, stack, b1, b2, l1[0], l1[1], i = [], [], [], [], 1, 1, 1
for q in range(0, (size ** 2) + 1, size): b1.append(q)
for q in range(1, (size ** 2) - (size - 2), size): b2.append(q)
wn.tracer(0)
rashi.speed(0)
while 0 in l1:
    if i not in b1 and l1[i + 1] == 0: neighbours.append(i + 1)
    if i not in b2 and l1[i - 1] == 0: neighbours.append(i - 1)
    if i + size < (size ** 2) and l1[i + size] == 0: neighbours.append(i + size)
    if i - size > 0 and l1[i - size] == 0: neighbours.append(i - size)
    if len(neighbours) > 0:
        m = random.choice(neighbours)
        if m == i + 1:
            x, y = rashi.xcor(), rashi.ycor()
            walls[i][1] = False
            l1[i + 1] = 1
            i += 1
            rashi.forward(15), neighbours.clear(), stack.append((rashi.xcor(), rashi.ycor()))
            if i == (size ** 2): om.goto(rashi.xcor(), rashi.ycor())
        elif m == i + size:
            x, y = rashi.xcor(), rashi.ycor()
            walls[i][3] = False
            l1[i + size] = 1
            i += size
            rashi.goto(x, y - 15), neighbours.clear(), stack.append((rashi.xcor(), rashi.ycor()))
        elif m == i - 1:
            x, y = rashi.xcor(), rashi.ycor()
            walls[i][0] = False
            l1[i - 1] = 1
            i -= 1
            rashi.goto(x - 15, y), neighbours.clear(), stack.append((rashi.xcor(), rashi.ycor()))
        elif m == i - size:
            x, y = rashi.xcor(), rashi.ycor()
            walls[i][2] = False
            l1[i - size] = 1
            i -= size
            rashi.goto(x, y + 15), neighbours.clear(), stack.append((rashi.xcor(), rashi.ycor()))
    else:
        m = stack.pop()
        rashi.penup(), rashi.goto(m), rashi.pendown()
        i = int((((rashi.xcor() + 140) / 15) + 1) + (((310 - rashi.ycor()) / 15) * size))
rashi.penup(), rashi.color("green"), rashi.goto(-140, 310)
solve.penup(), solve.goto(-140, 310), solve.color("blue"), solve.shape("square"), solve.shapesize(0.5, 0.5), solve.pencolor("blue"), solve.pendown()
messagebox.showinfo("information",
'''You can move around by using the arrow keys. On reaching the end press the right key or down key once to let the guard know that you want to go out. The maze will only be completed if you have the key''')
wn.tracer(1)
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.mainloop()
# journey_of_a_thousand_projects ¯\_(ツ)_/¯
# If you always look up to the sky you end up with wings to fly
# Not only should you practice your art but force your way into it's secrets
# ctrl + alt + s for changing settings
# I think my most efficient piece of code till now, I mean just see how compact it is, a mere 90 lines of code...
