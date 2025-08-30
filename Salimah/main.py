# import streamlit as st

# """
# # Hello World, Streamlit!

# This is a website to demonstrate Streamlit's API.
# You can stop looking at this now.

# Please.
# """

# st.write("This is some text made using Python.")

# adjective = st.text_input("Type in an adjective")
# noun = st.text_input("Type in a noun")
# verb = st.text_input("Type in a verb in past tense")

# st.write("I just gave a " + noun + " twenty " + adjective + " dollars and he " + verb + " me!")

# pressed = st.button("Press me!")
# if pressed:
#     st.write("Why did you do that?")

# pip install freegames
from turtle import *
from random import random
from freegames import line

def draw():
    """Draw maze."""
    color('black')
    width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    update()

def tap(x, y):
    """Draw line and dot for screen tap."""
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()
        width(2)
        color('red')
        goto(x, y)
        dot(4)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
