"""Even"""
def main():
    """Even"""
    num = int(input())
    for i in range(num+1):
        if i%2 == 1:
            print("Odd")
        if i%2 != 0:
            continue
        print(i)
main()
