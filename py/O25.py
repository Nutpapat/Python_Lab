"""Odd"""
def main():
    """Odd"""
    num = int(input())
    while True:
        if num%2 == 1:
            print(num, end=" ")
            num += 1
        else:
            print(num, end=" ")
            num = int(num/2)
        if num == 1:
            print(1)
            break
main()
