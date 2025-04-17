import turtle
import time
import random

# ----------------------- Game Setup -----------------------
win = turtle.Screen()
win.title("UniConda: Levels, Obstacles & Power-Ups!")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Turn off screen updates for manual control

# ----------------------- Snake Setup -----------------------
head = turtle.Turtle()
head.speed(0)  # Animation speed (0 = fastest)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = []  # Snake body segments

# ----------------------- Food Setup -----------------------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# ----------------------- Special Food (Power-Up) -----------------------
special_food = turtle.Turtle()
special_food.speed(0)
special_food.shape("triangle")
special_food.color("blue")
special_food.penup()
special_food.hideturtle()  # Initially hidden
special_food_active = False
special_food_duration = 7  # Seconds the special food stays on screen
special_food_spawn_time = 0  # Timestamp when special food was spawned

# ----------------------- Obstacles Setup -----------------------
obstacles = []  # List to hold obstacle turtles

def spawn_obstacles(level):
    """Spawn a number of obstacles based on the current level."""
    # First, clear old obstacles
    for obs in obstacles:
        obs.hideturtle()
    obstacles.clear()
    
    # Number of obstacles increases with level (3 per level)
    num_obstacles = level * 3
    for _ in range(num_obstacles):
        obs = turtle.Turtle()
        obs.speed(0)
        obs.shape("square")
        obs.color("brown")
        obs.penup()
        # Place obstacle in a random location avoiding edges (and center area)
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        obs.goto(x, y)
        obstacles.append(obs)

# ----------------------- Score & Level -----------------------
score = 0
high_score = 0
level = 1

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0  Level: 1", align="center", font=("Courier", 24, "normal"))

def update_score():
    pen.clear()
    pen.write("Score: {}  High Score: {}  Level: {}".format(score, high_score, level),
              align="center", font=("Courier", 24, "normal"))

# ----------------------- Movement Functions -----------------------
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 30)
    elif head.direction == "down":
        head.sety(head.ycor() - 10)
    elif head.direction == "left":
        head.setx(head.xcor() - 10)
    elif head.direction == "right":
        head.setx(head.xcor() + 10)

# ----------------------- Keyboard Bindings -----------------------
win.listen()
win.onkey(go_up, "i")
win.onkey(go_down, "k")
win.onkey(go_left, "j")
win.onkey(go_right, "l")

# ----------------------- Game Variables -----------------------
delay = 0.1  # Controls speed of snake

# Initially spawn obstacles for level 1 (can be no obstacles if you want)
spawn_obstacles(level)

# ----------------------- Main Game Loop -----------------------
while True:
    win.update()
    
    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide segments and obstacles as game reset
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        # Reset score and level (you can change this behavior if you want lives)
        score = 0
        level = 1
        delay = 0.1
        spawn_obstacles(level)
        update_score()

    # Check for collision with normal food
    if head.distance(food) < 20:
        # Move food to random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        
        # Add new segment to snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        if score > high_score:
            high_score = score
        
        # Increase level every 50 points
        if score % 50 == 0:
            level += 1
            spawn_obstacles(level)
        
        # Speed up the game gradually
        delay = max(0.05, delay - 0.006)
        update_score()

    # Check for collision with special food if active
    if special_food_active and head.distance(special_food) < 20:
        special_food.hideturtle()
        special_food_active = False
        score += 25  # Bonus points!
        if score > high_score:
            high_score = score
        update_score()

    # Spawn special food at random intervals (every 15-25 seconds)
    if not special_food_active and random.randint(1, 1000) == 1:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        special_food.goto(x, y)
        special_food.showturtle()
        special_food_active = True
        special_food_spawn_time = time.time()

    # Hide special food if it stays too long
    if special_food_active and time.time() - special_food_spawn_time > special_food_duration:
        special_food.hideturtle()
        special_food_active = False

    # Move the snake's body segments: last follows the one before it
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
        
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for collision with obstacles
    for obs in obstacles:
        if head.distance(obs) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            level = 1
            delay = 0.1
            spawn_obstacles(level)
            update_score()

    # Check for collision with itself
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            level = 1
            delay = 0.1
            spawn_obstacles(level)
            update_score()

    time.sleep(delay)
win.mainloop()
