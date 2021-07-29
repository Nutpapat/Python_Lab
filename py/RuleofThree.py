#NUTPAPAT YOUYOUNG 60070024
"""RuleofThree"""
def main():
    """This is Show Program Compare weight and price"""
    number_of_sizes = int(input())
    bestprice = 1
    bestweight = 1
    for _ in range(number_of_sizes):
        price = float(input())
        weight = float(input())
        if weight/price > bestweight/bestprice:
            bestprice = price
            bestweight = weight
        elif weight/price == bestweight/bestprice and price < bestprice:
            bestprice = price
            bestweight = weight
    print("%.2f %.2f" %(bestprice, bestweight))
main()
