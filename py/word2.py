""" Week 11 - 60070024 && 60070031 """
def main():
    """ WordSequence II """
    txt_1 = input()
    txt_2 = input()
    len_txt_1 = len(txt_1)
    len_txt_2 = len(txt_2)
    for i in range(0, len_txt_2+1):
        print(txt_2[0:i]+txt_1[i:len_txt_1+1])

    if len_txt_1 > len_txt_2:
        for i in range(0, len_txt_1-len_txt_2):
            print(txt_2+txt_1[len_txt_2+i+1:len_txt_1+1])
main()
