"""Catalan"""
def main():
    """cn+1 = (4n+2)/(n+2)*cn"""
    count = int(input())
    num = 1
    for i in range(count):
        num = ((4*i)+2)/(i+2)*num
    print(int(num))
main()
