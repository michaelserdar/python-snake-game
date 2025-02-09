#  snake game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#  setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake 2025 - Learning Python")
screen.tracer(0)  # needed for smooth animation of game

# creating the snake object three squares long
snake = Snake()

# creating the food pellet
food = Food()

# creating the scoreboard
scoreboard = Scoreboard()

# setting up the screen to listen for key commands
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game loop
game_is_on = True

while game_is_on:
    screen.update()  # graphics update after movement of segments
    time.sleep(0.1)  # delays the update at a consistent rate
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:  # slicing will access everything except the head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
