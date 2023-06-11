from turtle import Turtle, Screen
from random import randint
#Initialize game screen
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
# As user for a colour of turtle to bet (Red, Orange, yellow, green, blue and Violet
user_bet = screen.textinput(title="make your choice", prompt="Which color turtle will win the race 'Red, Yellow, Blue, Green, Violet & Orange', Enter the color: ")
color = ["violet", "blue", "green", "yellow", "orange", "red"]
turtles = []
yaxis = -100
# Place all turtles at the starting postion
for turt in color:
    tim = Turtle(shape = "turtle")
    tim.color(turt)
    tim.penup()
    tim.goto(x=-230,y=yaxis)
    turtles.append(tim)
    yaxis += 40
# check if user have given an input
if user_bet:
    is_race_on = True
# Starting of the main game loop
while is_race_on:
# Move turtle with different random speed at every steps
    for turt in turtles:
        if turt.xcor() > 230:
            winner = turt.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You won, The winner is {winner} turtle")
            else:
                print(f"You Lost, The winner is {winner} turtle")
        dist = randint(0,10)
        turt.forward(dist)
# exit game screen on click
screen.exitonclick()
