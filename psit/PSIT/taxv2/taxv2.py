"""TAX V2"""
def tax(money, sum_tax):
    """Print sum tax from given money"""
    sum_tax, money = find_tax(sum_tax, money, 4000000, 0.35)
    sum_tax, money = find_tax(sum_tax, money, 2000000, 0.30)
    sum_tax, money = find_tax(sum_tax, money, 1000000, 0.25)
    sum_tax, money = find_tax(sum_tax, money, 750000, 0.20)
    sum_tax, money = find_tax(sum_tax, money, 500000, 0.15)
    sum_tax, money = find_tax(sum_tax, money, 300000, 0.10)
    sum_tax, money = find_tax(sum_tax, money, 150000, 0.05)
    print(int(sum_tax))

def find_tax(sum_tax, money, cost, percen):
    """Find Tax of money"""
    sum_tax += max(0, ((money-cost)*percen))
    money = min(money, cost)
    return sum_tax, money

tax(int(input()), 0)
