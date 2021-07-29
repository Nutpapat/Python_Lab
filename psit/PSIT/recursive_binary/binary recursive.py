"""Recursion_Binary"""
def rec_binary(num, count):
    """Input number to changing by recursive fuction and print current
    function to last function"""
    count += 1
    if num > 0:
        rec_binary(num//2, count)
        print(num%2, end="")
    elif num == 0 and count == 1:
        print("0")
rec_binary(int(input()), 0)
