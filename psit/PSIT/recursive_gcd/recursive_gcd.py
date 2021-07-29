"""gcd_recursion"""
def recursive_gcd(num1, num2):
    """Input 2 number and check gcd by recursion"""
    if num2 == 0:
        return num1
    else:
        return recursive_gcd(num2, num1%num2)
print(recursive_gcd(int(input()), int(input())))
