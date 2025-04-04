#imports
import turtle
import pandas as pd

screen = turtle.Screen()                #Creates instance of screen object
screen.title("U.S. States Game")        #Adds title to screen
image = "blank_states_img.gif"          #Name/path of image file
screen.addshape(image)                  #Loads image to 'screen' and make available for turtle to display
turtle.shape(image)                     #Displays image

#Read states list to csv
df = pd.read_csv("50_states.csv")


#Variables
num_states_identified = 0
states_identified = []
incorrect = 0

while num_states_identified < len(df):
    state_in = screen.textinput(f"{num_states_identified}/50 States Correct",
                                "Enter a state").title()  # Creates textbox input Asking for state and converts input to title case
    print(state_in)
    if state_in in df.state.tolist():
        num_states_identified += 1
        state = df[df.state == state_in]
        state_name = state.state.values[0]
        states_identified.append(state_name)
        x_value = state.x.item()
        y_value = state.y.item()
        #y_value = state.y.values[0]
        #print(f"{state_name} -> {x_value} , {y_value}")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_value, y_value)
        t.pendown()
        t.write(state_name)

    else:
        incorrect += 1

print(states_identified)
print(f"{num_states_identified} incorrect choices.")





screen.exitonclick()
