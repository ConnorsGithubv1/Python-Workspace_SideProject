import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

# todo setup screen
wnd = turtle.Screen()
wnd.title("---Snake----")
wnd.bgcolor("grey")
wnd.setup(width=600, height=600)
wnd.tracer(0) # Turns off the screen updates

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
         head.direction = "left"


def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y= head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x= head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x= head.xcor()
        head.setx(x + 20)

#keyboard Bindings
wnd.listen()
wnd.onkeypress(go_up, "w")
wnd.onkeypress(go_down, "s")
wnd.onkeypress(go_right, "d")
wnd.onkeypress(go_left, "a")

# Main game Loop
while True:
    wnd.update()

    #check for a collison with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        wnd.bgcolor("red")
        time.sleep(1)
        wnd.bgcolor("grey")
        head.goto(0,0)
        head.direction = "stop"

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear segments list
        segments.clear()

        #reset score
        score = 0

        # reset delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for a collision with food
    if head.distance(food) < 20:
        #Move food to random spot
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        #shortens delay
        delay -= 0.001

        #increase score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # check for collison with body
    for segment in segments:
        if segment.distance(head) < 20:
            wnd.bgcolor("red")
            time.sleep(1)
            wnd.bgcolor("grey")
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            # clear segments list
            segments.clear()

            # reset score
            score = 0

            # reset delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wnd.mainloop()
