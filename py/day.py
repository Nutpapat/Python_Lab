"""Plan"""
def main(text, numx, numy, numz):
    """func_"""
    var1 = high(numx, numy, numz)
    var2 = low(numx, numy, numz)
    var3 = (numx+numy+numz)-(var1+var2)
    if text == "Ascend":
        print("%.2f, %.2f, %.2f" % (var2, var3, var1))
    elif text == "Descend":
        print("%.2f, %.2f, %.2f" % (var1, var3, var2))
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
main(str(input()), float(input()), float(input()), float(input()))
