"""Sequence IV"""
def main():
    """This is Show Program Number sequence"""
    var = int(input())
    num = 0
    for _ in range(var):
        for _ in range(var):
            num += 1
            print(num, end=" ")
        print()
main()
