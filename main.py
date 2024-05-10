import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("yellow")
screen.title("Epic Snake Game :)")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
screen.onkey(my_snake.left, 'Left')
screen.onkey(my_snake.right, 'Right')

my_scoreboard.update_score()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # detect collision with food
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_scoreboard.increase_score()  # count score

    # detect collision with wall
    if (my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290
            or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290):
        my_scoreboard.reset_highscore()
        my_snake.reset_snake()

    # detect collision with tail
    for piece_of_snake in my_snake.snake:
        if piece_of_snake == my_snake.head:
            pass
        elif my_snake.head.distance(piece_of_snake) < 10:
            my_scoreboard.reset_highscore()
screen.exitonclick()
