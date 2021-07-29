"""046: Parallelogram"""
def main():
    """cut word"""
    word = input()
    keep = ""
    long_word = len(word)
    for i in word:
        long_word -= 1
        space = " "*long_word
        keep += i
        print(space+keep)
    for j in range(len(word)-1):
        print(word[j+1:])
main()
