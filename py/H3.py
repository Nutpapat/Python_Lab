"""What"""
def main():
    """What!!!"""
    alp = input()
    num = int(input())
    print(' '*9+alp)
    print(' '*8+alp, alp)
    print(' '*7+alp, num, alp)
    print(' '*6+alp, str(abs(num-1))*3, alp)
    print(' '*5+alp, str(abs(num-2))*5, alp)
    print(' '*4+alp, str(abs(num-3))*7, alp)
    print(' '*3+alp, str(abs(num-4))*9, alp)
    print(' '*2+alp, str(abs(num-5))*11, alp)
    print(' '*1+alp, str(abs(num-6))*13, alp)
    print(alp*19 + '\nilluminaticonfirmed')
main()
