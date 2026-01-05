import turtle
import random
import time

# -------------------------
# Screen setup
# -------------------------
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Multi-Turtle Nighttime Fun 🌙🐢✨")
screen.setup(width=800, height=600)
screen.tracer(0)

# -------------------------
# Rainbow colors
# -------------------------
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# -------------------------
# Create turtles
# -------------------------
pink = turtle.Turtle()
pink.shape("turtle")
pink.color("pink")
pink.shapesize(2,2)
pink.penup()
pink.goto(-100, 0)

yellow = turtle.Turtle()
yellow.shape("turtle")
yellow.color("yellow")
yellow.shapesize(2,2)
yellow.penup()
yellow.goto(0,0)

green = turtle.Turtle()
green.shape("turtle")
green.color("lightgreen")
green.shapesize(2,2)
green.penup()
green.goto(100,0)

turtles = [pink, yellow, green]

# -------------------------
# Create stars (invisible initially)
# -------------------------
stars = []
for _ in range(15):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.color("white")
    star.goto(random.randint(-350,350), random.randint(-250,250))
    stars.append(star)

# -------------------------
# Raindrops
# -------------------------
raindrops = []
for _ in range(50):
    drop = turtle.Turtle()
    drop.hideturtle()
    drop.penup()
    drop.color("blue")
    drop.goto(random.randint(-400,400), random.randint(0,300))
    drop.dot(4)
    raindrops.append(drop)

# -------------------------
# Moon (appears at night)
# -------------------------
moon = turtle.Turtle()
moon.hideturtle()
moon.penup()
moon.color("lightyellow")
moon.goto(300,200)

# -------------------------
# Functions
# -------------------------
def rainbow_trail(t):
    trail = turtle.Turtle()
    trail.hideturtle()
    trail.penup()
    trail.goto(t.position())
    trail.pendown()
    trail.color(random.choice(rainbow_colors))
    trail.dot(8)

def sparkle_stars(t):
    for star in stars:
        if star.isvisible() and t.distance(star)<15:
            for size in [10,15,7]:
                star.dot(size,"yellow")
                screen.update()
                time.sleep(0.05)
            star.hideturtle()

def animate_rain():
    for drop in raindrops:
        drop.sety(drop.ycor() - 5)
        # bounce on all turtles
        for t in turtles:
            if abs(drop.xcor()-t.xcor()) < 20 and abs(drop.ycor()-t.ycor()) < 20:
                drop.sety(drop.ycor() + 10)
        if drop.ycor() < -300:
            drop.sety(random.randint(100,300))
            drop.setx(random.randint(-400,400))
        drop.showturtle()

# -------------------------
# Turtle movements
# -------------------------
def move_up(t): t.sety(t.ycor()+20)
def move_down(t): t.sety(t.ycor()-20)
def move_left(t): t.setx(t.xcor()-20)
def move_right(t): t.setx(t.xcor()+20)

# -------------------------
# Keyboard controls
# -------------------------
screen.listen()
# Pink turtle
screen.onkey(lambda: move_up(pink), "Up")
screen.onkey(lambda: move_down(pink), "Down")
screen.onkey(lambda: move_left(pink), "Left")
screen.onkey(lambda: move_right(pink), "Right")
# Yellow turtle
screen.onkey(lambda: move_up(yellow), "w")
screen.onkey(lambda: move_down(yellow), "s")
screen.onkey(lambda: move_left(yellow), "a")
screen.onkey(lambda: move_right(yellow), "d")
# Green turtle
screen.onkey(lambda: move_up(green), "i")
screen.onkey(lambda: move_down(green), "k")
screen.onkey(lambda: move_left(green), "j")
screen.onkey(lambda: move_right(green), "l")

# -------------------------
# Day-to-night transition
# -------------------------
def fast_night_transition():
    # Colors from day to night
    colors = ["#87CEEB", "#6495ED", "#1E90FF", "#00008B", "#000033"]
    for c in colors:
        screen.bgcolor(c)
        screen.update()
        time.sleep(0.3)
    # show moon
    moon.showturtle()
    # show stars
    for star in stars:
        star.showturtle()

# -------------------------
# Main loop
# -------------------------
fast_night_transition()  # start with night
while True:
    for t in turtles:
        rainbow_trail(t)
        sparkle_stars(t)
    animate_rain()
    screen.update()
