from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, board_w, board_h):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.penup()
        self.board_w = board_w
        self.board_h = board_h
        x = random.randint(-0.95*board_w/2, 0.95*board_w/2)
        y = random.randint(-0.95*board_h/2, 0.95*board_h/2)
        self.goto(x, y)

    def move(self):
        new_x = random.randint(-0.95*self.board_w/2, 0.95*self.board_w/2)
        new_y = random.randint(-0.95*self.board_h/2, 0.95*self.board_h/2)
        self.goto(new_x, new_y)
