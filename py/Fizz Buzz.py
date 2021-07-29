"""Fizz Buzz"""
def main():
    """This is show output Fizz Buzz"""
    count = int(input())
    for i in range(1, count+1):
        if i%3 == 0 and i%5 == 0:
            i = "Fizz Buzz"
        elif i%3 == 0:
            i = "Fizz"
        elif i%5 == 0:
            i = "Buzz"
        print(i)
main()
