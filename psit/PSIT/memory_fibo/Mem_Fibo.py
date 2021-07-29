"""Fibonacci Mem Problem"""
def fibo(number, data):
    """Return fibonacci values for given number"""
    if number in data:
        return data[number]
    res = fibo(number-2, data) + fibo(number-1, data)
    data[number] = res
    return res

print(fibo(int(input()), {0:0, 1:1}))
