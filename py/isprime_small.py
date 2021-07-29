"""isprime_small"""
def main():
    """This is show program isprime_small"""
    num = int(input())
    mod = 0
    check = 0
    if num >= 2:
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                mod += 1
                check += 1
            if check > 2:
                break
    if mod == 1:
        print("YES")
    elif mod > 1:
        print("NO")
    else:
        print("NO")
main()
