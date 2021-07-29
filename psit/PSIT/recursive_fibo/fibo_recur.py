"""Fibonacci Problem"""
def fibo(number):
    """Return fibonacci from you given number."""
    if number > 1:
        return fibo(number - 1) + fibo(number - 2)
    elif number == 1:
        return number
    else:
        return number
print(fibo(int(input())))
