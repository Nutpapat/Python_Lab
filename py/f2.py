"""Ascending"""
def main():
    """This is show program Ascending"""
    list1 = []
    for _ in range(5):
        num = int(input())
        list1.append(int(num))
        list1.sort()
    for i in list1:
        print(i)
main()
