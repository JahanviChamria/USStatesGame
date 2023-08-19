from turtle import Turtle, Screen
import turtle
import pandas

screen=Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed=[]
while len(guessed)<50:
    ans=screen.textinput(title=f"{len(guessed)}/50 States Correct", prompt="Enter a name: ")
    anst=ans.title()
    states=pandas.read_csv("50_states.csv")
    st=states["state"].to_list()
    score=0
    if anst=="Exit":
        missing=[]
        for s in st:
            if s not in guessed:
               missing.append(s)
        newdata=pandas.DataFrame(missing)
        newdata.to_csv("learn.csv")
        break
    if anst in st:
        t=Turtle()
        t.hideturtle()
        t.penup()
        statedata=states[states.state==anst]
        t.goto(int(statedata["x"]), int(statedata["y"]))
        t.write(anst)
        guessed.append(anst)


