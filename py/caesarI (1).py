"""CaesarI"""
def main():
    """Decoder"""
    slide = int(input())
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = "abcdefghijklmnopqrstuvwxyz"
    text = input()
    for i in text:
        if i.isalpha():
            if i.isupper():
                print(big[(big.find(i)+slide)%26], end="")
            else:
                print(small[(small.find(i)+slide)%26], end="")
        else:
            print(i, end="")
main()
