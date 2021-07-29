"""Integer"""
def main():
    """Integer"""
    count = 0
    nsum = 0
    while True:
        num = input()
        if num.isdigit():
            count += int(num)
            nsum += 1
        else:
            break
    if nsum == 0:
        print("Python is very Ez")
    else:
        print("Sum of number is", count)
        print("Average is : %.2f" %(count/nsum))
main()
