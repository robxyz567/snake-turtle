from turtle import Screen
from snake import Snake
from food import Food
from messages import Message
import time


TIME_DELAY = 0.07
BOARD_W = 480
BOARD_H = 480


screen = Screen()
screen.setup(width=BOARD_W, height=BOARD_H)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = []
snake.append(Snake())
snake[0].goto(0, 0)

food = Food(BOARD_W, BOARD_H)

message = Message((0, 0.75*BOARD_H/2))
points = 0
message.score_update(points)

screen.listen()
screen.onkey(snake[0].left, "Left")
screen.onkey(snake[0].right, "Right")
screen.onkey(snake[0].up, "Up")
screen.onkey(snake[0].down, "Down")

game_is_on = True
while game_is_on:

    screen.update()

    if len(snake) > 4:
        for i in range(4, len(snake)):
            if snake[0].distance(snake[i]) < 15:
                message.game_over()
                game_is_on = False

    if len(snake) > 1:
        for i in range(len(snake)-1, 0, -1):
            snake[i].goto(snake[i - 1].pos())

    if snake[0].xcor() > BOARD_W/2-5 or snake[0].xcor() < -BOARD_W/2+5:
        message.game_over()
        game_is_on = False
    if snake[0].ycor() > BOARD_H/2-5 or snake[0].ycor() < -BOARD_H/2+5:
        message.game_over()
        game_is_on = False

    if snake[0].distance(food) < 15:
        points += 1
        food.move()
        if points > message.high_score:
            message.high_score = points
            message.update_file(points)
        message.score_update(points)
        snake.append(Snake())

    snake[0].moving()

    time.sleep(TIME_DELAY)

screen.exitonclick()