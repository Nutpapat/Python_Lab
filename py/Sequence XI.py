"""Sequence XI"""
def main():
    """Sequence XI"""
    num = int(input())
    num2 = 1
    num_c = 2*num-2
    num_3 = 0
    for i in range(1, num+1):
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        for i in range(num2, num2+1):
            print(("%02d " %i)*num_c, end="")
        num2 += 1
        num_c -= 2
        for i in range(num_3, 0, -1):
            print("%02d" %i, end=" ")
        num_3 += 1
        print()
    num2 = num-1
    num_c = 2
    for i in range(1, num):
        for j in range(1, num+1-i):
            print("%02d" %j, end=" ")
        for i in range(num2, num2-1, -1):
            print(("%02d " %i)*num_c, end="")
        for i in range(num2-1, 0, -1):
            print("%02d" %i, end=" ")
        num2 -= 1
        num_c += 2
        print()
main()
