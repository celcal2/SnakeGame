from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_snake_up(), "Up")
screen.onkey(snake.move_snake_down, "Down")
screen.onkey(snake.move_snake_left, "Left")
screen.onkey(snake.move_snake_right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move_snake()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increac_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.all_snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()