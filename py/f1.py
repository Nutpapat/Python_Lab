"""Fibonacci_v1"""
def main():
    """This is show program Fibonacci_v1"""
    num = int(input())
    num0 = 0
    num1 = 1
    if num <= 30:
        for _ in range(num-1):
            num2 = num1+num0
            num0 = num1
            num1 = num2
        print(num1)
main()
