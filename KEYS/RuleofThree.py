"""
PSIT Pair-Programming (21/Sep/2017)
#1 - Teerapat Kraisrisirikul (60070183)
#2 - Siwakorn Lertamnuaylap (60070095)
"""
 
def main():
    """ Main function """
    price_best = -1
    weight_best = -1
    value_best = -1
 
    for _ in range(int(input())):
        price, weight = float(input()), float(input())
        value = weight/price
 
        if value > value_best or (value == value_best and price < price_best):
            value_best, price_best, weight_best = value, price, weight
 
    print("%.2f %.2f" % (price_best, weight_best))
 
main()