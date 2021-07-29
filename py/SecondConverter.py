"""Hamburger"""
def main():
    """This is show program output"""
    left = int(input())
    right = int(input())
    left1 = "|"*left
    right1 = "|"*right
    cen = (left+right)*2
    cen1 = "*"*cen
    print(left1+ cen1+ right1)
main()
