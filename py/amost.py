"""Duplicate I"""
def main():
    """same student ID"""
    lst = []
    same = []
    num_m = int(input())
    num_n = int(input())
    for i in range(num_n+num_m):
        if i < num_m:
            lst.append(input())
        else:
            tmp = input()
            if tmp in lst:
                same.append(tmp)
                lst.append(tmp)
    if same == []:
        print('Nope')
    else:
        for i in sorted(same, reverse=True):
            print(i)
main()
