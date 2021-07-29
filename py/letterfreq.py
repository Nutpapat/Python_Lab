"""LetterFrequency"""
def main():
    """Frequency letter"""
    text = input().lower()
    dct = {}
    lst = []
    for i in text:
        if i.isalpha():
            dct[i] = text.count(i)
    for keys in dct:
        var = dct[keys]
        lst.append(var)
        lst.sort(reverse=True)
    for values in dct:
        if dct[values] == lst[0]:
            print(values)
main()
