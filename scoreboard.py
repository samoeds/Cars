from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-260, 205)
        self.level = 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-80, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)


    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)