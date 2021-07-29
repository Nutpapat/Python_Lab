"""Bill"""
def main():
    """This is show program Bill"""
    bill = int(input())
    bill1 = bill*0.1
    bill2 = 50
    bill3 = 1000
    bill4 = (bill+bill2)*0.07
    bill5 = (bill+bill3)*0.07
    bill6 = (bill+bill1)*0.07
    if bill1 < 50:
        print("%.2f" %(bill+bill2+bill4))
    elif bill1 > 1000:
        print("%.2f" %(bill+bill3+bill5))
    else:
        print("%.2f" %(bill+bill1+bill6))
main()
