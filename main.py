import pandas as pd
import turtle
from scoreboard import Scoreboard
data = pd.read_csv(r"C:\Users\wifi.MUBSP41149\Documents\David\Curso Python\Day 25\us-states-game-start\50_states.csv")
screen = turtle.Screen()
screen.title("The US. States Game")
image = r"C:\Users\wifi.MUBSP41149\Documents\David\Curso Python\Day 25\us-states-game-start\blank_states_img_1.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()
states = data["state"].to_list()
cursor = turtle.Turtle()
cursor.penup()
cursor.hideturtle()
while True:
    if scoreboard.points == 50:
        scoreboard.finish()
        turtle.mainloop()
        break
    answer_state = screen.textinput(title= "Guess the State", prompt= "What's another state's name?").title()

    if answer_state == "Exit":
        states_missed = {"States missed": states}
        missed_states = pd.DataFrame(states_missed)
        missed_states.to_csv("States Missed.csv")
        break

    if answer_state in states:
        line = data[data["state"] == answer_state]
        x, y = int(line["x"]), int(line["y"])
        cursor.goto(x,y)
        cursor.write(answer_state)
        scoreboard.clear()
        scoreboard.new_score()
        states.remove(answer_state)






