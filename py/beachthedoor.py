"""BreachTheDoor"""
def main():
    """cut word"""
    text = input()+" "
    wordchk = ""
    keep = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    big = alpha.upper()
    check = alpha+big
    for i in text:
        if i in check:
            wordchk += i
        else:
            if len(wordchk) > 6:
                keep += wordchk+" "
                wordchk = ""
            else:
                wordchk = ""
    print(keep)
main()

