"""CoinChange1"""
def coinchange(num, count):
    """Input number of changing, Output number of coin to change"""
    while num > 0:
        if num >= 25:
            num = num - 25
            count += 1
        elif num >= 10:
            num = num - 10
            count += 1
        elif num >= 5:
            num = num - 5
            count += 1
        elif num >= 1:
            num = num - 1
            count += 1
    print(count)
 
coinchange(int(input()), 0)
