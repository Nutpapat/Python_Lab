"""Sequence VI"""
def main():
    """this is show output"""
    num = int(input())
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    for i in range(1, num):
        for j in range(1, num+1-i):
            print(j, end=" ")
        print()
main()
