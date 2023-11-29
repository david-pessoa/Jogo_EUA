from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(90, 250)
        self.points = 0
        self.new_score()
    
    def new_score(self):
        self.write(arg = f"Points: {self.points}/50", font = FONT,)
        self.points += 1
    
    def finish(self):
        self.home()
        self.color("blue")
        self.write(arg ="CONGRATULATIONS!", font = ("Arial", 30, "normal"), align = "center")