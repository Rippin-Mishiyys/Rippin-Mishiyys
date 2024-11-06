import turtle

# Mortar size (space between the squares)
MORTAR_SIZE = 2

# Draw a line from (x1, y1) to (x2, y2)
def draw_line(x1, y1, x2, y2, color):
    pen_state = turtle.pen()
    turtle.pencolor(color)
    turtle.width(2)  # Make the line for the X thicker to be more visible
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.up()
    turtle.pen(pen_state)

# Draw a rectangle with the upper left corner at (x, y)
# and with dimensions x_size by y_size. Use color for the background.
def draw_rect(x, y, x_size, y_size, color):
    pen_state = turtle.pen()
    turtle.fillcolor(color)
    turtle.pencolor("black")  # Keep border of the square black
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.setheading(90)
    turtle.begin_fill()
    turtle.forward(x_size)
    turtle.right(90)
    turtle.forward(y_size)
    turtle.right(90)
    turtle.forward(x_size)
    turtle.right(90)
    turtle.forward(y_size)
    turtle.end_fill()
    turtle.up()
    turtle.pen(pen_state)

# Function to draw a single square
def draw_square(x, y, size, color):
    draw_rect(x, y, size, size, color)

# Function to draw an "X" inside a square
def draw_x_in_square(x, y, size):
    padding = 3  # Padding from the edge to make the X visible inside
    top_left = (x + padding, y - padding)
    top_right = (x + size - padding, y - padding)
    bottom_left = (x + padding, y - size + padding)
    bottom_right = (x + size - padding, y - size + padding)
    
    # Draw the "X" inside the square
    draw_line(top_left[0], top_left[1], bottom_right[0], bottom_right[1], "blue")  # Diagonal from top-left to bottom-right
    draw_line(top_right[0], top_right[1], bottom_left[0], bottom_left[1], "blue")  # Diagonal from top-right to bottom-left

# Function to draw a row of alternating black and white squares with mortar spacing
def draw_row(x, y, num_squares, size):
    for i in range(num_squares):
        color = "black" if i % 2 == 0 else "white"
        draw_square(x + i * (size + MORTAR_SIZE), y, size, color)

# Function to draw "X" inside a row of squares with mortar spacing
def draw_x_in_row(x, y, num_squares, size):
    for i in range(num_squares):
        draw_x_in_square(x + i * (size + MORTAR_SIZE), y, size)

# Function to draw the entire grid with mortar spacing
def draw_grid(start_x, start_y, rows, cols, size):
    for i in range(rows):
        draw_row(start_x, start_y - i * (size + MORTAR_SIZE), cols, size)

# Function to draw "X"s in the entire grid with mortar spacing
def draw_x_in_grid(start_x, start_y, rows, cols, size):
    for i in range(rows):
        draw_x_in_row(start_x, start_y - i * (size + MORTAR_SIZE), cols, size)

# Main function to replicate the pattern from the image
def draw_pattern():
    square_size = 30

    # Draw top left (1x6)
    draw_row(-300, 150, 6, square_size)
    draw_x_in_row(-300, 150, 6, square_size)

    # Draw middle left (2x5)
    draw_grid(-300, 90, 2, 5, square_size)
    draw_x_in_grid(-300, 90, 2, 5, square_size)

    # Draw bottom left (6x6)
    draw_grid(-300, -90, 6, 6, square_size)
    draw_x_in_grid(-300, -90, 6, 6, square_size)

    # Draw top right (4x4)
    draw_grid(30, 150, 4, 4, square_size)
    draw_x_in_grid(30, 150, 4, 4, square_size)

    # Draw middle right (5x3)
    draw_grid(150, 50, 5, 3, square_size)
    draw_x_in_grid(150, 50, 5, 3, square_size)

    # Draw bottom right (5x5)
    draw_grid(150, -150, 5, 5, square_size)
    draw_x_in_grid(150, -150, 5, 5, square_size)

# Set up the screen with a width of 650 and a height of 400
screen = turtle.Screen()
screen.setup(width=650, height=400)
screen.bgcolor("gray")

# Set up turtle
turtle.speed(0)
turtle.hideturtle()

# Call the main drawing function
draw_pattern()

# Finish
turtle.done()


