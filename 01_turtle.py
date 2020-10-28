#!/usr/bin/python3
"""
First example of using the turtle graphics library in Python
Drawing the shape of a square of side length 400

Gilberto Echeverria
26/03/2019
"""

# Declare the module to use
import turtle

#Draw a square, around the center
side = 400

# Move right
turtle.forward(side/2)
# Turn to the left
turtle.left(90)
# Move up
turtle.forward(side/2)
# Turn to the left
turtle.left(90)
# Move left
turtle.forward(side)
# Turn to the left
turtle.left(90)
# Move down
turtle.forward(side)
# Turn to the left
turtle.left(90)
# Move right
turtle.forward(side)
# Turn to the left
turtle.left(90)
# Move up
turtle.forward(side/2)

# Start the drawing loop
turtle.done()
