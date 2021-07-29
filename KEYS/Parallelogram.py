"""
PSIT - Week 13
Teerapat Kraisrisirikul (60070183)
"""
 
def main():
    """ Main function """
    text = input()
    _ = [print((len(text)-len(text[0:i]))*" "+text[0:i]) for i in range(1, len(text))]
    _ = [print(text[i::]+(len(text)-len(text[i::]))*" ") for i in range(0, len(text))]
 
main()