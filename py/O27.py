"""My heart"""
def main():
    """My heart"""
    num = 1
    while num:
        num = input()
        if num.isdigit():
            continue
        else:
            num = str(num)
            if num.find("a") != -1 or num.find("e") != -1 or num.find("i") != -1 or \
            num.find("o") != -1 or num.find("u") != -1:
                continue
            else:
                print(num)
                break
main()
