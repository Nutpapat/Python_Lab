"""BinaryLab"""
def b_inary_10(dec):
    """print Binary number from Decimal"""
    count = 0
    list_b_inary = []
    if dec == 0:
        print(0)
    while dec > 1:
        count = dec%2
        dec = dec//2
        list_b_inary.append(count)
    if dec == 1:
        list_b_inary.append(dec)
    list_b_inary.reverse()
    for i in list_b_inary:
        print(i, end="")
b_inary_10(int(input()))
