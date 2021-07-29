"""036"""

def main():
    """Completed"""
    num = int(input())
    for i in range(1, 2 * num):
        if i <= num:
            for j in range((num - i + 1), num):
                print("%02d" % j, end=" ")
            for j in range(num, (i - 1), -1):
                print("%02d" % j, end=" ")
            for j in range((i +1), (num + 1)):
                print("%02d" % j, end=" ")
            for j in range((num - 1), (num - i), -1):
                print("%02d" % j, end=" ")
        else:
            for j in range((i - num + 1), num):
                print("%02d" % j, end=" ")
            for j in range(num, ((num * 2) - i - 1), -1):
                print("%02d" % j, end=" ")
            for j in range(num - (i - num - 1), (num + 1)):
                print("%02d" % j, end=" ")
            for j in range((num - 1), (i - num), -1):
                print("%02d" % j, end=" ")
        print("" * (num > 1) * (i > 1))
main()
