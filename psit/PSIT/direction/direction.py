"""FourDirection Problem"""
def direction(string):
    """Print Direction from input"""
    for loop in range(5):
        for word in string:
            if word == "U":
                up_direction(loop)
            elif word == "D":
                down_direction(loop)
            elif word == "L":
                left_direction(loop)
            else:
                right_direction(loop)
        print()
 
def up_direction(loop):
    """Print DirectionUP of loop"""
    if loop == 0 or loop == 3 or loop == 4:
        print("  *  ", end=" ")
    elif loop == 1:
        print(" *** ", end=" ")
    elif loop == 2:
        print("* * *", end=" ")
 
def down_direction(loop):
    """Print DirectionDOWN of loop"""
    up_direction(4-loop)
 
def left_direction(loop):
    """Print DirectionLEFT of loop"""
    if loop == 0 or loop == 4:
        print("  *  ", end=" ")
    elif loop == 1 or loop == 3:
        print(" *   ", end=" ")
    elif loop == 2:
        print("*****", end=" ")
 
def right_direction(loop):
    """Print DirectionRIGHT of loop"""
    if loop == 0 or loop == 4:
        print("  *  ", end=" ")
    elif loop == 1 or loop == 3:
        print("   * ", end=" ")
    elif loop == 2:
        print("*****", end=" ")
 
direction(input())
