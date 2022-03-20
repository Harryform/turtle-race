import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
screen.bgcolor("black")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

if user_bet:
    is_race_on = True

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! {winning_color} won! ")
            else:
                print(f"You lose! The {winning_color} turtle was the winner. ")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)




screen.exitonclick()
