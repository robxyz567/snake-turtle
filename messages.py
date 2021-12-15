from turtle import Turtle


class Message(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        with open("scores.txt") as file:
            try:
                self.high_score = int(file.read())
            except:
                self.high_score = 0

    def score_update(self, points):
        self.clear()
        self.write(arg=f'Score: {points}\nBest score: {self.high_score}', align="center", font=("Courier", 16, "normal"))

    def update_file(self, points):
        with open("scores.txt", mode="w") as file:
            file.write(str(points))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align="center", font=("Courier", 30, "normal"))

