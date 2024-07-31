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
number_of_enemies = 10
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
    if enemy_number == 5:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 2

# Create the player's bullets
bullets = []
for _ in range(2):
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()
    bullets.append(bullet)

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstates = ["ready", "ready"]

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
    for i in range(len(bullets)):
        if bulletstates[i] == "ready":
            bulletstates[i] = "fire"
            x = player.xcor()
            y = player.ycor() + 10
            bullets[i].setposition(x, y)
            bullets[i].showturtle()
            break

def is_collision(t1, t2):
    distance = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
    return distance < 15

def check_win():
    for enemy in enemies:
        if enemy.isvisible():
            return False
    return True

# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
    for enemy in enemies:
        if enemy.isvisible():
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            if enemy.xcor() > 280 or enemy.xcor() < -280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemyspeed *= -1

            if is_collision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("Game Over")
                break

    for i in range(len(bullets)):
        if bulletstates[i] == "fire":
            y = bullets[i].ycor()
            y += bulletspeed
            bullets[i].sety(y)

        if bullets[i].ycor() > 275:
            bullets[i].hideturtle()
            bulletstates[i] = "ready"

        for enemy in enemies:
            if is_collision(bullets[i], enemy):
                bullets[i].hideturtle()
                bulletstates[i] = "ready"
                bullets[i].setposition(0, -400)
                enemy.hideturtle()

    if check_win():
        win_pen = turtle.Turtle()
        win_pen.color("white")
        win_pen.penup()
        win_pen.hideturtle()
        win_pen.setposition(0, 0)
        win_pen.write("YOU WIN", align="center", font=("Arial", 36, "normal"))
        break

turtle.done()