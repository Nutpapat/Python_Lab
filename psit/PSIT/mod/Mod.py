"""MOD Problem"""
def mod(loop):
    """Return number of max(factor)"""
    list_number = []
    list_factor = []
    for _ in range(loop):
        number = int(input())
        fac = count_factor(number)
        list_number.append(number)
        list_factor.append(fac)
    for num in range(len(list_factor)):
        if list_factor[num] == max(list_factor):
            print(list_number[num])

def count_factor(number):
    """Return count(factor) of number"""
    list_factor = []
    for num in range(1, int(number//2)+1):
        if number % num == 0:
            list_factor.append(int(number/num))
            list_factor.append(num)
    return len(list_factor)

mod(int(input()))
