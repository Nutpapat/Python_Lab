""" Week 11 - 60070024 && 60070031 """
def main(text):
    """RemoveTag"""
    lst_intag = []
    lengthoftext = len(text)
    for i in range(lengthoftext):
        if text[i] == '<':
            for j in range(i, len(text)):
                if text[j] == '>':
                    lst_intag.append(text[i:j+1])
                    break

    for tag in lst_intag:
        text = text.replace(tag, ' ')
    text = text.replace('\t', ' ')
    print(text.split())
main(input())
