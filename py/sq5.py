"""BootSequence"""
def main():
    """print(i_)"""
    num = int(input())
    text = 0
    for i in range(num, 0, -1):
        print(i, end=" ")
        text += 1
        if text % 7 == 0:
            print()

main()