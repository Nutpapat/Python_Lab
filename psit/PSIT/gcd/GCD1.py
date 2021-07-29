'''[RECURSIVE] GCD'''
def is_fibo(num1, num2):
    '''Return GCD from num.'''
    while num1 != 0:
        num1, num2 = num2%num1, num1
    print(num2)

is_fibo(int(input()), int(input()))
