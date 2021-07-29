""" Week 11 - 60070024 && 60070031 """
def main():
    """ WordSequence I """
    txt = input()
    len_txt = len(txt)
    for i in range(1, len_txt+1):
        print(txt[0:i])
main()
