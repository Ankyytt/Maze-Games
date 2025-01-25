import random
import time
import turtle
from tkinter import messagebox

size = int(turtle.numinput("Size of maze", "Enter Size:", 35, minval=30, maxval=45))
name = str(turtle.textinput("Getting to know you", "What's your name :"))
wn = turtle.Screen()
wn.bgcolor("black"), wn.setup(800, 720), wn.tracer(0)


def initial_animation(writing=("Presenting to " + name, "with happiness heart-felt", "a genuine effort", "By Ankit Das", "The Labyrinth of destinies"), chosen_font="jokerman", t=3):
    animate = turtle.Turtle()
    animate.hideturtle()
    animate.penup()
    x_animate = 200
    for wr in writing:
        animate.pencolor("blue")
        for wr1 in range(1, 63):
            animate.goto(0, x_animate)
            animate.write("{}".format(wr), align="center", font=(chosen_font, wr1, "bold"))
            time.sleep(0.1)
            if wr1 < 35: x_animate += 1.5
            elif 35 < wr1 < 49: x_animate -= 3
        animate.pencolor("orange")
        if wr == "By Ankit Das": animate.pencolor("lime")
        if wr == "The Labyrinth of destinies": animate.pencolor("magenta"); t = 8
        animate.write("{}".format(wr), align="center", font=(chosen_font, 63, "bold"))
        time.sleep(t)
        animate.clear()


initial_animation()
key = turtle.Turtle()
coin = turtle.Turtle()
clone_node = turtle.Turtle()
clone_wealth = turtle.Turtle()
hut = turtle.Turtle()
step = turtle.Turtle()
pf = turtle.Turtle()
e1, e2, e3, e4 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()

e1.shape("classic"), e2.shape("classic"), e3.shape("classic"), e4.shape("classic")
e1.color("red"), e2.color("red"), e3.color("red"), e4.color("red")
e1.penup(), e2.penup(), e3.penup(), e4.penup()
e1.hideturtle(), e2.hideturtle(), e3.hideturtle(), e4.hideturtle()
e2.right(180), e3.right(270), e4.right(90)

r = random.randint(int((size ** 2) / 3), int((size ** 2) / 1.5))  # random location of the node of power
r1 = random.randint(size, int((size ** 2) / 3))  # random location for the ending red hut
r2 = random.randint(int((size ** 2) / 1.2), size ** 2)  # random location for the node of wealth
r3 = random.randint(1, size - 1)  # random location of the start camp

key_taken, coin_taken, kills, won, hunted, p = False, False, False, False, 0, 0

key_x, key_y = - 140 + (r % size) * 15, 310 - ((r - (r % size)) / size) * 15
coin_x, coin_y = - 140 + (r2 % size) * 15, 310 - ((r2 - (r2 % size)) / size) * 15
om_x, om_y = - 140 + (r1 % size) * 15, 310 - ((r1 - (r1 % size)) / size) * 15
start_x, start_y = - 140 + (r3 % size) * 15, 310 - ((r3 - (r3 % size)) / size) * 15

key.color("cyan"), key.shapesize(0.5, 0.5), key.shape("triangle"), key.penup(), key.goto(key_x, key_y)
coin.color("white"), coin.shapesize(0.5, 0.5), coin.shape("circle"), coin.penup(), coin.goto(coin_x,
                                                                                             coin_y), coin.hideturtle()
clone_node.penup(), clone_node.color("cyan"), clone_node.goto(-500, 250), clone_node.write("Node of power",
                                                                                           align="left", font=(
        "jokerman", 30, "normal")), clone_node.shape("triangle"), clone_node.color("cyan"), clone_node.shapesize(2.5,
                                                                                                                 2.5), clone_node.goto(
    -550, 270)
clone_wealth.penup(), clone_wealth.color("white"), clone_wealth.goto(-500, 190), clone_wealth.write("Node of wealth",
                                                                                                    align="left", font=(
        "jokerman", 30, "normal")), clone_wealth.shape("circle"), clone_wealth.color("white"), clone_wealth.shapesize(
    2.5,
    2.5), clone_wealth.goto(
    -550, 210)
hut.penup(), hut.color("red"), hut.goto(-500, 130), hut.write("The red hut", align="left",
                                                              font=("jokerman", 30, "normal")), hut.shape(
    "square"), hut.color("red"), hut.shapesize(2.5, 2.5), hut.goto(-550, 150)
step.penup(), step.goto(-550, 70), step.color("lime"), step.hideturtle()
pf.hideturtle(), pf.penup()


def up():  # This allows me to move in the up direction
    try:
        global key_taken, p, coin_taken, steps, kills, won  # to maintain consistency of value in every function
        p = int((((solve.xcor() + 140) / 15) + 1) + (
                ((310 - solve.ycor()) / 15) * size))  # determine the location of solver on the maze
        x_cor = solve.xcor()
        y_cor = solve.ycor()
        if steps > 0:
            if walls[p][2] is False or walls[p - size][3] is False:  # checks for the presence of walls
                y_cor += 15
                solve.sety(y_cor)
                steps -= 1
            if (x_cor, y_cor) == (key_x, key_y) and not key_taken:
                eat()
                key.hideturtle(), coin.showturtle()
                key_taken = True
                solve.color("cyan")
            if (x_cor, y_cor) == (coin_x, coin_y) and key_taken and not coin_taken:
                eat()
                coin.hideturtle(), om.showturtle()
                coin_taken = True
                solve.color("purple")
            if (x_cor, y_cor) == (e2.xcor(), e2.ycor()):
                e2.hideturtle()
                eat()
                pf.clear()
            if (x_cor, y_cor) == (om.xcor(), om.ycor()) and key_taken and coin_taken and not won:
                om.color("green")
                eat()
                om.hideturtle()
                won = True
                steps = 10000
                messagebox.showinfo("Congratulations",
                                    "You have reached the hut of the wizard, "
                                    "The wizard gives you infinite health and unseen path-finding skills best of luck and use these well "
                                    "press h to start the hunt( you can hunt as many spirits as you feel like) and press q when you are done")
        else:
            if not kills: kill(solve.xcor(), solve.ycor())
    except KeyError:
        pass  # do nothing if the user is trying to hit a wall or something of that sort


def down():
    global p, key_taken, coin_taken, steps, kills, won
    try:
        p = int((((solve.xcor() + 140) / 15) + 1) + (((310 - solve.ycor()) / 15) * size))
        x_cor = solve.xcor()
        y_cor = solve.ycor()
        if steps > 0:
            if walls[p][3] is False or walls[p + size][2] is False:
                y_cor -= 15
                solve.sety(y_cor)
                steps -= 1
            if (x_cor, y_cor) == (key_x, key_y) and not key_taken:
                eat()
                key.hideturtle(), coin.showturtle()
                key_taken = True
                solve.color("cyan")
            if (x_cor, y_cor) == (coin_x, coin_y) and key_taken and not coin_taken:
                eat()
                coin.hideturtle(), om.showturtle()
                coin_taken = True
                solve.color("purple")
            if (x_cor, y_cor) == (e2.xcor(), e2.ycor()):
                e2.hideturtle()
                eat()
                pf.clear()
            if (x_cor, y_cor) == (om.xcor(), om.ycor()) and key_taken and coin_taken and not won:
                om.color("green")
                eat()
                om.hideturtle()
                won = True
                steps = 10000
                messagebox.showinfo("Congratulations",
                                    "You have reached the hut of the wizard, "
                                    "The wizard gives you infinite health and unseen path-finding skills best of luck and use these well "
                                    "press h to start the hunt( you can hunt as many spirits as you feel like) and press q when you are done")
        else:
            if not kills: kill(solve.xcor(), solve.ycor())
    except KeyError:
        pass


def right():
    global key_taken, p, coin_taken, steps, kills, won
    try:
        p = int((((solve.xcor() + 140) / 15) + 1) + (((310 - solve.ycor()) / 15) * size))
        x_cor = solve.xcor()
        y_cor = solve.ycor()
        if steps > 0:
            if walls[p][1] is False or walls[p + 1][0] is False:
                x_cor += 15
                solve.setx(x_cor)
                steps -= 1
            if (x_cor, y_cor) == (key_x, key_y) and not key_taken:
                eat()
                key.hideturtle(), coin.showturtle()
                key_taken = True
                solve.color("cyan")
            if (x_cor, y_cor) == (coin_x, coin_y) and key_taken and not coin_taken:
                eat()
                coin.hideturtle(), om.showturtle()
                coin_taken = True
                solve.color("purple")
            if (x_cor, y_cor) == (e2.xcor(), e2.ycor()):
                eat()
                e2.hideturtle()
                pf.clear()
            if (x_cor, y_cor) == (om.xcor(), om.ycor()) and key_taken and coin_taken and not won:
                om.color("green")
                eat()
                om.hideturtle()
                won = True
                steps = 10000
                messagebox.showinfo("Congratulations",
                                    "You have reached the hut of the wizard, "
                                    "The wizard gives you infinite health and unseen path-finding skills best of luck and use these well "
                                    "press h to start the hunt( you can hunt as many spirits as you feel like) and press q when you are done")
        else:
            if not kills: kill(solve.xcor(), solve.ycor())
    except KeyError:
        pass


def left():
    try:
        global key_taken, p, coin_taken, steps, kills, won
        p = int((((solve.xcor() + 140) / 15) + 1) + (((310 - solve.ycor()) / 15) * size))
        x_cor = solve.xcor()
        y_cor = solve.ycor()
        if steps > 0:
            if walls[p][0] is False or walls[p - 1][1] is False:
                x_cor -= 15
                solve.setx(x_cor)
                steps -= 1
            if (x_cor, y_cor) == (key_x, key_y) and not key_taken:
                eat()
                key.hideturtle(), coin.showturtle()
                key_taken = True
                solve.color("cyan")
            if (x_cor, y_cor) == (coin_x, coin_y) and key_taken and not coin_taken:
                eat()
                coin.hideturtle(), om.showturtle()
                coin_taken = True
                solve.color("purple")
            if (x_cor, y_cor) == (e2.xcor(), e2.ycor()):
                eat()
                e2.hideturtle()
                pf.clear()
            if (x_cor, y_cor) == (om.xcor(), om.ycor()) and key_taken and coin_taken and not won:
                om.color("green")
                eat()
                om.hideturtle()
                won = True
                steps = 10000
                messagebox.showinfo("Congratulations",
                                    "You have reached the hut of the wizard, "
                                    "The wizard gives you infinite health and unseen path-finding skills best of luck and use these well "
                                    "press h to start the hunt( you can hunt as many spirits as you feel like) and press q when you are done")
        else:
            if not kills: kill(solve.xcor(), solve.ycor())
    except KeyError:
        pass


def quit_game():  # just to allow you to end the game if you want to
    try:
        global steps
        if not won:
            if steps > 0:
                messagebox.showerror("Shame",
                                     "You are a coward and no more, now see what happens to cowards in this realm")
                steps = -1
                kill(solve.xcor(), solve.ycor())
                die(solve)
            else:
                die(solve)
                messagebox.showerror("Alas...", "You have been eaten up by the evil spirits")
        else:
            messagebox.showinfo("Thank-you", "you have been brave and helped us kill the spirits... thank-you so much")
        turtle.bye()
    except:
        pass


def eat():
    solve.color("yellow")
    for s_solve in range(20, 8, -1):
        solve.shapesize(s_solve / 20, s_solve / 20)
        time.sleep(0.05)


def die(square):
    for s_solve in range(8, 0, -1):
        square.shapesize(s_solve / 20, s_solve / 20)
        time.sleep(0.05)


def step_check():
    global steps
    step.clear()
    step.write("Steps Left {}".format(steps), align="left", font=("consolas", 25, "bold"))
    time.sleep(2)
    step.clear()


def kill(x_k, y_k):
    global kills
    try:
        if not kills:
            e1.goto(x_k - 15, y_k), e2.goto(x_k + 15, y_k), e3.goto(x_k, y_k - 15), e4.goto(x_k, y_k + 15)
            kills = True
            suck(e1, 40)
            suck(e2, 30)
            suck(e3, 30)
            suck(e4, 30)
            quit_game()
    except:
        pass


def suck(x_suck, s):
    try:
        x_suck.showturtle()
        time.sleep(1)
        x_suck.forward(10)
        for it in range(8, s):
            x_suck.shapesize(it / 20, it / 20)
            time.sleep(0.1)
        x_suck.color("red")
        x_suck.pencolor("black")
        x_suck.shapesize(s / 20, s / 20, s / 20)
        time.sleep(1)
    except:
        pass


def path_find(dic, start, end, size_path, b1_path, b2_path, dic1, color, pathfinder):
    try:
        pathfinder.penup()
        pathfinder.goto(start)
        pathfinder.pendown()
        pathfinder.speed(0)
        for ran in range(1, size_path ** 2 + 1): dic1[ran] = False
        possibility = []
        stack_path = []
        steps_path = 0
        loc_start = int((((pathfinder.xcor() + 140) / 15) + 1) + (((310 - pathfinder.ycor()) / 15) * size_path))
        if start not in [(key_x, key_y), (coin_x, coin_y)]: dic1[loc_start] = True
        while (pathfinder.xcor(), pathfinder.ycor()) != end:
            loc = int((((pathfinder.xcor() + 140) / 15) + 1) + (((310 - pathfinder.ycor()) / 15) * size_path))
            if loc not in b1_path and (dic[loc][1] is False or dic[loc + 1][0] is False) and visited[
                loc + 1] is False: possibility.append(loc + 1)
            if loc not in b2_path and (dic[loc][0] is False or dic[loc - 1][1] is False) and visited[
                loc - 1] is False: possibility.append(loc - 1)
            if loc + size_path < (size_path ** 2) and (dic[loc][3] is False or dic[loc + size_path][2] is False) and \
                    visited[loc + size_path] is False: possibility.append(loc + size_path)
            if loc - size_path > 0 and (dic[loc][2] is False or dic[loc - size_path][3] is False) and visited[
                loc - size_path] is False: possibility.append(loc - size_path)
            if len(possibility) > 0:
                pathfinder.pencolor(color)
                m_path = random.choice(possibility)
                if m_path == loc + 1:
                    x_path, y_path = pathfinder.xcor(), pathfinder.ycor()
                    stack_path.append((x_path, y_path))
                    steps_path += 1
                    loc += 1
                    dic1[loc] = True
                    pathfinder.forward(15), possibility.clear()
                elif m_path == loc + size_path:
                    x_path, y_path = pathfinder.xcor(), pathfinder.ycor()
                    stack_path.append((x_path, y_path))
                    steps_path += 1
                    loc += size_path
                    dic1[loc] = True
                    pathfinder.goto(x_path, y_path - 15), possibility.clear()
                elif m_path == loc - 1:
                    x_path, y_path = pathfinder.xcor(), pathfinder.ycor()
                    stack_path.append((x_path, y_path))
                    steps_path += 1
                    loc -= 1
                    dic1[loc] = True
                    pathfinder.goto(x_path - 15, y_path), possibility.clear()
                elif m_path == loc - size_path:
                    x_path, y_path = pathfinder.xcor(), pathfinder.ycor()
                    stack_path.append((x_path, y_path))
                    steps_path += 1
                    loc -= size_path
                    dic1[loc] = True
                    pathfinder.goto(x_path, y_path + 15), possibility.clear()
            else:
                pathfinder.pencolor("black")
                m_path = stack_path.pop()
                steps_path -= 1
                pathfinder.goto(m_path)
        return steps_path
    except Exception:
        try:
            messagebox.showerror("Error !!", "Sorry something went wrong please restart the game")
            turtle.bye()
        except:
            turtle.bye()


def prepare(sp1):
    r_sp1 = random.randint(1, size ** 2 - 1)
    sp1.goto(- 140 + (r_sp1 % size) * 15, 310 - ((r_sp1 - (r_sp1 % size)) / size) * 15)
    sp1.shapesize(0.5, 0.5)


def hunt():
    if won:
        wn.tracer(0), e2.shape("circle"), pf.clear()
        prepare(e2)
        e2.showturtle()
        path_find(walls, (solve.xcor(), solve.ycor()), (e2.xcor(), e2.ycor()), size, b1, b2, visited, "magenta", pf)
        wn.tracer(1), solve.pendown(), solve.pencolor("black")


def rules():
    messagebox.showinfo("Rules, Fresh from the garden", '''
1. Arrow keys to move
2. S to see the number of steps left
3. H to begin the hunt (Works only if you have the spells from the wizard)
4. Q to quit the game
5. R to see the rules''')


visited = {}
solve = turtle.Turtle()
om = turtle.Turtle()
x, y = -147, 332
om.pencolor("dark grey"), om.pensize(6), om.hideturtle(), om.speed(0)
for i in range(1, size + 1):
    x = -147
    y -= 15
    for j in range(1, size + 1):
        om.penup(), om.goto(x, y), om.pendown(), om.forward(15), om.right(90), om.forward(15), om.right(90), om.forward(
            15), om.right(90), om.forward(15), om.right(90)
        x += 15
om.penup(), om.goto(-155, 245), om.hideturtle(), om.shape("square"), om.shapesize(0.7, 0.7, 0.5), om.color("red")
l1 = []
walls = {}
for i in range((size ** 2) + 1):
    l1.append(0)
    walls[i] = [True, True, True, True]
rashi = turtle.Turtle()
rashi.penup(), rashi.pensize(9), rashi.shape("square"), rashi.shapesize(0.5, 0.5, 0.5), rashi.goto(-140,
                                                                                                   310), rashi.pendown(), rashi.color(
    "white"), rashi.pencolor("black")
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
            rashi.forward(15), neighbours.clear(), stack.append((x, y))
        elif m == i + size:
            x, y = rashi.xcor(), rashi.ycor()
            walls[i][3] = False
            l1[i + size] = 1
            i += size
            rashi.goto(x, y - 15), neighbours.clear(), stack.append((x, y))
        elif m == i - 1:
            x, y = rashi.xcor(), rashi.ycor()
            walls[i][0] = False
            l1[i - 1] = 1
            i -= 1
            rashi.goto(x - 15, y), neighbours.clear(), stack.append((x, y))
        elif m == i - size:
            x, y = rashi.xcor(), rashi.ycor()
            walls[i][2] = False
            l1[i - size] = 1
            i -= size
            rashi.goto(x, y + 15), neighbours.clear(), stack.append((x, y))
    else:
        m = stack.pop()
        rashi.penup(), rashi.goto(m), rashi.pendown()
        i = int((((rashi.xcor() + 140) / 15) + 1) + (((310 - rashi.ycor()) / 15) * size))
rashi.penup(), rashi.color("green"), rashi.goto(start_x, start_y), om.goto(om_x, om_y)
solve.penup(), solve.goto(start_x, start_y), solve.color("pink"), solve.shape("square"), solve.shapesize(0.4,
                                                                                                         0.4), solve.pencolor(
    "pink")
wn.tracer(0)
s1 = path_find(walls, (start_x, start_y), (key_x, key_y), size, b1, b2, visited, "black", pf)
s2 = path_find(walls, (key_x, key_y), (coin_x, coin_y), size, b1, b2, visited, "black", pf)
s3 = path_find(walls, (coin_x, coin_y), (om_x, om_y), size, b1, b2, visited, "black", pf)
steps = s1 + s2 + s3 + 2 * size
messagebox.showinfo("Trouble Trouble Trouble !",
                    "You wake up and find yourself in a strange maze. hungry and weak you can walk no more than a few steps even if you used your last ounce of strength. "
                    "but With the evil spirits on your trail you have no option but find your way in this strange world. "
                    "You have to reach the red hut, because there lives the greedy wizard who in exchange for money would willingly cast you a spell or two... "
                    "But beware that the spirits are spying on you..."
                    "The moment they know that you are weak and can not walk, they attack..."
                    "good luck and  always remember, without the node of power there is no node of wealth and without wealth there is no home")
messagebox.showinfo("Rules will help",
                    '''You can move around by using the arrow keys. The maze will only be completed if you reach the hut. The starting camp is symbolised by green. Press q to quit the game and press s to see the no of steps you can afford to take. press R to see the rules.''')
wn.tracer(1)
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(quit_game, "q")
wn.onkeypress(step_check, "s")
wn.onkeypress(hunt, "h")
wn.onkeypress(rules, "r")
wn.mainloop()
# Cheers to my dream of becoming the best in the world of coding
# journey_of_a_thousand_projects ¯\_(ツ)_/¯
# If you always look up to the sky you end up with wings to fly
# Not only should you practice your art but force your way into it's secrets
# I think my most efficient piece of code till now, I mean just see how compact it is, a mere 500 lines of code...
