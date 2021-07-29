"""SecondConverter"""
def main():
    """This function is show output"""
    size = int(input())
    place = input()
    text = input()
    line = abs(size-len(text))
    if place == "left":
        print((text)+(line*" "))
    elif place == "right":
        print((line*" ")+(text))
    elif place == "center":
        if line%2 == 1:
            print(" "+text.center(size-1))
        elif line%2 == 0:
            print(text.center(size))
main()
