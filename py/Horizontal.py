"""Horizontal histogram"""
def main():
    """print histogram"""
    text = input()
    box = {}
    for i in text:
        if i.isalpha():
            box[i] = text.count(i)
    for j in sorted(box):
        if j.islower():
            print(j, ("-----|"*(box[j]//5) + "-----|"[:box[j]%5]).rstrip('|'), sep=' : ')
    for j in sorted(box):
        if j.isupper():
            print(j, ("-----|"*(box[j]//5) + "-----|"[:box[j]%5]).rstrip('|'), sep=' : ')
main()
