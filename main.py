from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

game_is_on = True
snake = Snake()
snake.create_snake()

screen.onkey(snake.move_snake_up(), "Up", )
screen.onkey(snake.move_snake_down()"Down")
screen.onkey(snake.move_snake_left(), "Left")
screen.onkey(snake.move_snake_right(), "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()