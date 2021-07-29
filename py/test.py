"""Sequence I"""
def main():
    """This is Show Program Number sequence"""
    number = int(input())
    for i in range(1, number+1):
        for i in range(1, number+1):
            print(i, end=" ")
        print()
main()