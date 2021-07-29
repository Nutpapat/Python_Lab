"""Sequence VIII"""
def main():
    """This fucntion is show output"""
    num = int(input())
    text = 0
    for i in range(1, num+1):
        text = (" "*(num-i))+("0"+str(i))
        print(text)
main()
