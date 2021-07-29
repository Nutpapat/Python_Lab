"""IterationBinary"""
def ite_binary(num):
    """Input number to edit to become the binary number."""
    list_binary = [1]
    list_test = []
    if num == 0:
        list_binary = []
        print(0)
    while num != 0 and num != 1:
        if num%2 == 1:
            list_test.append(1)
        elif num%2 == 0:
            list_test.append(0)
        num = num//2
    list_test.reverse()
    list_binary.extend(list_test)
    for i in list_binary:
        print(i, end="")
ite_binary(int(input()))
