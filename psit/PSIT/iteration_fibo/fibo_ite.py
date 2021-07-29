"""Fibonacci Problem"""
def fibo(number):
    """Return fibonacci from you given number."""
    if number == 1 or number == 0:
        return number
    else:
        mem = {0:0, 1:1}
        for i in range(2, number+1):
            mem[i] = mem[i-1]+mem[i-2]
        return mem[number]
print(fibo(int(input())))
