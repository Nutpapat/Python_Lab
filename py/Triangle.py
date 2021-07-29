"""Triangle I"""
def main(numx, numy, numz):
    """func_"""
    var1 = high(numx, numy, numz)
    var2 = low(numx, numy, numz)
    var3 = (numx+numy+numz)-(var1+var2)
    if 0 <= abs(var1**2 - (var2**2+var3**2)) <= 0.01 and var1 > 0 and var2 > 0 and var3 > 0:
        print("Yes")
    else:
        print("No")
def high(val1, val2, val3):
    """check high"""
    if val1 >= val2 and val1 >= val3:
        return val1
    elif val2 >= val1 and val2 >= val3:
        return val2
    elif val3 >= val1 and val3 >= val2:
        return val3
def low(val1, val2, val3):
    """check low"""
    if val1 <= val2 and val1 <= val3:
        return val1
    elif val2 <= val1 and val2 <= val3:
        return val2
    elif val3 <= val1 and val3 <= val2:
        return val3
main(float(input()), float(input()), float(input()))
