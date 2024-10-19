import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the turtle's attributes
my_turtle.shape("turtle")  # Set turtle shape
my_turtle.color("green")  # Set turtle color
my_turtle.speed(2)  # Set movement speed (1 is slow, 10 is fast)

# Move the turtle forward
my_turtle.forward(100)

# Turn the turtle to the right
my_turtle.right(90)

# Move the turtle forward again
my_turtle.forward(100)

# Hide the turtle after movement
my_turtle.hideturtle()

# Keep the window open until it's clicked
turtle.done()
