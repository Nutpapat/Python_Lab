#NUTPAPAT YOUYOUNG 60070024
"""Sequence XII"""
def main(num):
    """This is Show Program Compare Pressurize"""
    num1 = num
    num2 = 1
    if 0 < num < 100:
        for i in range(num):
            for i in range(num1, num):
                print("%02d " %i, end='')
            num1 -= 1
            for i in range(num, num2, -1):
                print("%02d " %i, end='')
#                num2 += 1
            for i in range(num2, num):
                print("%02d " %i, end='')
            num2 += 1
            for i in range(num, num1, -1):
                print("%02d " %i, end='')
            print('')
        num1 = 2
        num2 = num-1
        for i in range(num-1):
            for i in range(num1, num):
                print("%02d " %i, end='')
            #num1 += 1
            for i in range(num, num2, -1):
                print("%02d " %i, end='')
            for i in range(num2, num):
                print("%02d " %i, end='')
            num2 -= 1
            for i in range(num, num1-1, -1):
                print("%02d " %i, end='')
            num1 += 1
            print('')
main(int(input()))
