"""Donut"""
def main():
    """This is show program Donut"""
    price = int(input())
    buy = int(input())
    free = int(input())
    must = int(input())

    buy1 = must // (buy+free)
    donut = buy1 * (buy+free)
    must %= buy+free

    pay = buy1*price*buy

    if must >= buy:
        buy1 = must // buy
        donut += buy1 * (buy+free)
        pay += buy1 * buy * price

    else:
        donut += must
        pay += must * price

    print(pay, donut)
main()

