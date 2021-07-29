"""OneTwo Problem"""
def one_two(number):
    """Return Sn number"""
    if number == 1:
        return str(1)
    elif number == 2:
        return 2
    else:
        return str(one_two(number - 1)) + str(one_two(number - 2))
print(one_two(int(input())))
