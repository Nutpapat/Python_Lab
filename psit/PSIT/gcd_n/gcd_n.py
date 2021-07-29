"""GCD_N_Lab"""
def gcd_list(num):
    """Input number of N(num) and input N as number"""
    list_n = []
    for _ in range(num):
        numbercount = int(input())
        list_n.append(numbercount)
    return list_n

def gcd_n(num):
    """finding a number of greatest common divisor """
    list_number = gcd_list(num)
    list_ans = []
    list_maxans = []
    for i in list_number:
        for j in range(1, i+1):
            if i%j == 0:
                list_ans.append(j)
    for i in list_ans:
        if list_ans.count(i) == num:
            list_maxans.append(i)
    print(max(list_maxans))
gcd_n(int(input()))
