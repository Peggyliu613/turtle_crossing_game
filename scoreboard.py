from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def go_to_next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
