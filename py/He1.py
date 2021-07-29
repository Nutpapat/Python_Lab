"""screen"""
def main():
    """screen"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    text = input()
    if num1 >= 3:
        print("-" * num1)
        print(("|"+(" "*(num1-2))+("\n"))*(num2-3))
    if num3 >= 0:
        print("|%s|" %text)
    if num3 <= 0:
        print("|%-s|" %text)
    if 1 <= num2 <= 3:
    	print(text)
    if 1 <= num1 <= 8:
    	print(text)
    else:
    	print("-" * num1)
main()
