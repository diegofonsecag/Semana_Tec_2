"""
Simple tests to learn how to use the 'turtle.circle' method

Gilberto Echeverria
16/02/2018
"""

import sys
import turtle


def draw_polygon(radius, segments):
    """ Draw a polygon of the number of sides """
    # Set the position of the cursor on the side of the circle
    initialize_position(radius)
    turtle.circle(radius, steps=segments)


def draw_circle(radius, segments, colors):
    """ Draw a circle using the number of segments indicated.
        Each segment is drawn with a different color, taken from the array """
    # Set the position of the cursor on the side of the circle
    initialize_position(radius)
    arc_angle = 360 / segments
    for i in range(segments):
        turtle.pencolor( colors[i % len(colors)] )
        turtle.circle(radius, arc_angle)


def configure_pen():
    """ Set the desired speed and pen size for the drawing """
    turtle.speed(1)
    turtle.pensize(2)
    turtle.shape("turtle")
    #turtle.hideturtle()


def initialize_position(radius):
    """ Set a new position to start drawing a circle """
    turtle.penup()
    turtle.setposition(radius, 0)
    turtle.pendown()
    turtle.setheading(90)


def get_segments():
    """ Check if the user provided an argument for the number of segments """
    if len(sys.argv) > 1:
        num_segments = int(sys.argv[1])
    else:
        num_segments = 8
    return num_segments


def main():
    """ Initial function to setup the drawing """
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
    radius = 200
    num_segments = get_segments()
    configure_pen()
    draw_polygon(radius, num_segments)
    draw_circle(radius, num_segments, colors)
    # Start the drawing loop
    turtle.done()


main()
