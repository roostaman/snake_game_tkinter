import turtle as t

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


def read_score():
    with open('/Users/rustam/Desktop/PieProjects/PRO2/snake_game.py/data.txt', 'r') as file:
        content = file.read()
        return content


def write_score(add_score):
    with open('/Users/rustam/Desktop/PieProjects/PRO2/snake_game.py/data.txt', 'w') as file:
        file.write(add_score)


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(x=0, y=270)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | Highscore: {read_score()}", align=ALIGNMENT, font=FONT)

    def increase_score(self, points=1):
        self.score += points
        self.update_score()

    def reset_highscore(self):
        high_s = int(read_score())
        if self.score > high_s:
            write_score(str(self.score))
        self.score = 0
        self.update_score()
