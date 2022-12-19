import turtle, random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)




turtles = []
colours = ["red", "orange", "yellow", "green", "blue", "purple"]





y = -120



for num in range(len(colours)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colours[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    turtles.append(new_turtle)
    y += 50

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

if user_bet:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() < 230:
            move = random.randint(0, 10)
            turtle.forward(move)
        else:
            game_on = False
            
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You lose. The {winning_color} turtle won ")
            else:
                print(f"You lose. The {winning_color} turtle won ")









screen.exitonclick()