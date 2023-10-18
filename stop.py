#Turtle Graphics: Draw a traffic sign with the word "STOP" in the center
#by Nestor Soto 

# Import the turtle module to use turtle graphics

import turtle

# Define the function to draw a traffic sign
def draw_traffic_sign(size, center_x):
    # Nested function to draw the octagon part of the traffic sign
    def draw_octagon():
        turtle.color("red")  # Set the color to red
        turtle.begin_fill()  # Start filling the drawn shape with the specified color
        for _ in range(8):  # Loop 8 times to draw an octagon
            turtle.forward(size)  # Move the turtle forward by the specified size
            turtle.left(45)  # Turn the turtle left by 45 degrees
        turtle.end_fill()  # End filling the drawn shape

    # Nested function to draw the pole part of the traffic sign
    def draw_pole():
        turtle.color("gray")  # Set the color to gray
        turtle.begin_fill()  # Start filling the drawn shape with the specified color
        for _ in range(2):  # Loop 2 times to draw a rectangle
            turtle.forward(size // 5)  # Move the turtle forward by one-fifth of the specified size
            turtle.left(90)  # Turn the turtle left by 90 degrees
            turtle.forward(size * 1.5)  # Move the turtle forward by 1.5 times the specified size
            turtle.left(90)  # Turn the turtle left by 90 degrees
        turtle.end_fill()  # End filling the drawn shape

    # Nested function to write "STOP" text in the center of the octagon
    def write_stop():
        turtle.penup()  # Lift the pen up to move without drawing
        turtle.goto(center_x, size * 0.9)  # Move to the center of the octagon
        turtle.pendown()  # Put the pen down to start drawing/writing
        turtle.color("white")  # Set the color to white
        turtle.write("STOP", align="center", font=("Arial", int(size * 0.5), "bold"))  # Write the word "STOP" with specified font settings

    turtle.speed(0)  # Set the drawing speed to the fastest

    # Draw the octagon
    turtle.penup()  # Lift the pen up to move without drawing
    turtle.goto(center_x - size / 2, 0)  # Move to the starting position
    turtle.pendown()  # Put the pen down to start drawing
    draw_octagon()  # Call the draw_octagon function to draw the octagon

    # Draw the pole beneath the octagon
    turtle.penup()  # Lift the pen up to move without drawing
    turtle.goto(center_x - size // 10, -size * 1.5)  # Move to the starting position to draw the pole
    turtle.pendown()  # Put the pen down to start drawing
    draw_pole()  # Call the draw_pole function to draw the pole

    # Write "STOP" in the center of the octagon
    write_stop()  # Call the write_stop function to write "STOP"

# Call the draw_traffic_sign function with the specified size and center_x to draw the first traffic sign
draw_traffic_sign(100, 0)

# Call the draw_traffic_sign function with the specified size and center_x to draw the second traffic sign
draw_traffic_sign(75, 250)  # The center_x is 200 units to the right of the center of the first one

# Finish the drawing
turtle.done()
turtle.Screen().exitonclick()
