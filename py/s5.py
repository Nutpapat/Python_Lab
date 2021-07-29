"""Sequence IX"""
def main():
    """This is Show Program Number sequence"""
    number = int(input())
    for i in range(1, number+1):
        print(" " * (number-i)*3, end="")
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        for j in range(i-1, 0, -1):
            print("%02d" %j, end=" ")
        print()
    for i in range(1, number):
        print(" " * (i*3), end="")
        for j in range(1, number-i+1):
            print("%02d" %j, end=" ")
        for j in range(number-i-1, 0, -1):
            print("%02d" %j, end=" ")
        print()
main()
