
print( "Welcome to the Shape Generator:" )
cont = True
shape1 = 0
shape2 = 0
shape3 = 0
shape4 = 0
shape5 = 0
shape6 = 0
drawAnotherShape = False


def menu():
    print()
    print( "This program draw the following shapes:" )
    print( f"{'1) Horizontal Line':>20s}" )
    print( f"{'2) Vertical Line':>18s}" )
    print( f"{'3) Rectangle':>14s}" )
    print( f"{'4) Left slant right angle triangle':>36s}" )
    print( f"{'5) Right slant right angle triangle':>37s}" )
    print( f"{'6) Isosceles triangle':>23s}" )


def printShape1(length):
    print( f"Here is the horizontal line with length {length}:" )
    for i in range( length ):
        print( "*", end="" )
    print()


def printShape2(length):
    print( f"Here is the vertical line with length {length}:" )
    for i in range( length ):
        print( "*" )


def printShape3(length, width):
    print( f"Here is the rectangle with length {length} and width {width}:" )
    for x in range( length ):
        for x in range ( width):
            print( "*",end="")
        print()


def printShape4(height):
    print( f"Here is the left slant right angle triangle with height {height}:" )
    for x in range( 1, height + 1 ):
        for y in range (x):
            print( "*", end="")
        print()


def printShape5(height):
    print( f"Here is the right slant right angle triangle with height {height}:" )
    for x in range( 1, height + 1 ):
        print( " " * (height - x), end=" " )
        for y in range (x):
            print( "*", end="" )
        print()


def printShape6(height):
    print( f"Here is the isosceles triangle with height {height}:" )
    for x in range( 1, height + 1 ):
        for y in range (height - x + 1):
            print( " " , end="" )
        for z in range(x * 2 - 1):
            print( "*", end="")
        print()

def inputLength():
    length = int( input( "Enter the length of the shape (1-20): " ) )
    while length < 1 or length > 20:
        print( "Invalid input! You must enter a dimension between 1 and 20." )
        length = int( input( "Enter the length of the shape (1-20): " ) )
    return length


def inputWidth():
    width = int( input( "Enter the width of the rectangle (1-20): " ) )
    while width < 1 or width > 20:
        print( "Invalid input! You must enter a dimension between 1 and 20." )
        width = int( input( "Enter the width of the rectangle (1-20): " ) )
    return width


def inputHeight():
    height = int( input( "Enter the height of the shape triangle (1-20): " ) )
    while height < 1 or height > 20:
        print( "Invalid input! You must enter a dimension between 1 and 20." )
        height = int( input( "Enter the height of the shape (1-20): " ) )
    return height


def inputDrawAnotherShape():
    drawAnotherShape = input( "Would you like to draw another shape (y/n)? " )
    while drawAnotherShape != "Y" and drawAnotherShape != "y" and drawAnotherShape != "N" and drawAnotherShape != "n":
        print( "Error! Incorrect input. Please enter 'y','Y','n' or 'N' to continue." )
        drawAnotherShape = input( "Would you like to draw another shape (y/n)? " )
    if drawAnotherShape == "Y" or drawAnotherShape == "y":
        cont = True
    else:
        cont = False
    return cont

def goodbye():
    print()
    print( "***************************************************************" )
    print( "Here is a summary of the shapes that were drawn." )
    print()
    print( f"Horizontal Line {shape1:45d}" )
    print( f"Vertical Line {shape2:47d}" )
    print( f"Rectangle {shape3:51d}" )
    print( f"Left Slant Right Angle Triangle {shape4:29d}" )
    print( f"Right Slant Right Angle Triangle {shape5:28d}" )
    print( f"Isosceles Triangle {shape6:42d}" )
    print()
    print( "Thank you for using the Shape Generator! Goodbye!" )
    print( "***************************************************************" )

while cont == True:

    menu()

    shape = int( input( "Enter your choice (1-6): " ) )
    while shape < 1 or shape > 6:
        print( "Invalid choice! Your choice must be between 1 and 6." )
        shape = int( input( "Enter your choice (1-6): " ) )

    if shape == 1:
        shape1 += 1
        length = inputLength()
        printShape1( length )

    elif shape == 2:
        shape2 += 1
        length = inputLength()
        printShape2( length )

    elif shape == 3:
        shape3 += 1
        length = inputLength()
        width = inputWidth()
        printShape3( length, width )

    elif shape == 4:
        shape4 += 1
        height = inputHeight()
        printShape4( height )

    elif shape == 5:
        shape5 += 1
        height = inputHeight()
        printShape5( height )

    elif shape == 6:
        shape6 += 1
        height = inputHeight()
        printShape6( height )

    cont = inputDrawAnotherShape()

goodbye()

