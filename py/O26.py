"""Multi"""
def main():
    """Multi"""
    number = int(input())
    for i in range(1, 13):
        if i < 10:
            print("%d X %d  = %d" %(number, i, number*i))
        else:
            print("%d X %d = %d" %(number, i, number*i))
main()
