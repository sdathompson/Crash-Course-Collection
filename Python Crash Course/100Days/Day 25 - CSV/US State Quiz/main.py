import turtle
import pandas
from states import States

#Instructions: run and type states in that you know

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
statesClass = States()


while len(statesClass.guessed_states) < 50:
# Pop-up window that stores the user input into answer_state
    answer_state = screen.textinput(title=f"{len(statesClass.guessed_states)}/50 states guessed", prompt="Guess a state name").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in statesClass.guessed_states:
                statesClass.missing_states.append(state)

        states_to_learn = pandas.DataFrame(statesClass.missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    # If answer_state is one of the states in all the states
        #If they got it right:
    if answer_state in all_states:
        statesClass.guessed_states.add(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Select the row with the answer
        state_coord = state_data[state_data.state == answer_state]
        t.goto(state_coord.x.item(), state_coord.y.item())
        #Create a turtle to write the name of the state at the coords
            # Pandas.item() looks into the data and grabs the first element
        t.write(f"{state_coord.state.item()}", align="center", font= ("Times New Roman", 8 , "normal"))

# states_to_learn.csv




# # Get the co-ordinates of a mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# # Alternative way to keep the screen open
# turtle.mainloop()

