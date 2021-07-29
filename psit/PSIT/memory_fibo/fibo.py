"""Fibonacci_Memory"""
dict1 = {0:0, 1:1}
def fibonacci_mem(num):
    """Input number and checking by dictionnary"""
    if num in dict1:
        return dict1[num]
    res = fibonacci_mem(num-1) + fibonacci_mem(num-2)
    dict1[num] = res
    return res
print(fibonacci_mem(int(input())))
