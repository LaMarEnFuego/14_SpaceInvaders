import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width=800, height=600)

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set up the player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Choose the number of enemies
number_of_enemies = 5
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

# Create enemies
for enemy in enemies:
    enemy.color(random.choice(["red", "green", "yellow", "purple", "white"]))
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    enemy_number += 1

enemyspeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

# Create obstacles
obstacles = []
number_of_obstacles = 3
obstacle_start_x = -150

for i in range(number_of_obstacles):
    obstacle = turtle.Turtle()
    obstacle.color("brown")
    obstacle.shape("square")
    obstacle.penup()
    obstacle.speed(0)
    x = obstacle_start_x + (150 * i)
    y = -150
    obstacle.setposition(x, y)
    obstacles.append(obstacle)

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
    return distance < 15

# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            enemy.setposition(0, 10000)

        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

turtle.done()