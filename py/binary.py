"""Binary"""
def main():
    """This is show program Binary"""
    num = int(input())
    list1 = []
    if num == 0:
        list1.append(0)
    while num >= 1:
        list1.append(num%2)
        num = num//2
    list1.reverse()
    for i in list1:
        print(i, end="")
main()
