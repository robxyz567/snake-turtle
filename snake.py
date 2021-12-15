from turtle import Turtle

MOVE_CONSTANT = 15


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green yellow")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.penup()
        self.x_move = MOVE_CONSTANT
        self.y_move = MOVE_CONSTANT

    def moving(self):
        self.forward(MOVE_CONSTANT)

    def left(self):
        if self.heading() == 0:
            pass
        else:
            self.setheading(180)

    def right(self):
        if self.heading() == 180:
            pass
        else:
            self.setheading(0)

    def up(self):
        if self.heading() == 270:
            pass
        else:
            self.setheading(90)

    def down(self):
        if self.heading() == 90:
            pass
        else:
            self.setheading(270)
