"""Inflation"""
def main():
    """This is show program to think of inflation"""
    money = float(input())
    year = int(input())
    money = int(money*100)
    for _ in range(year):
        money = ((money*10381)//10000)
    print("%d.%.02d" %(money//100, money%100))
main()
