""" Week 11 - 60070024 && 60070031 """
def main(deep, width):
    """Diamond1"""
    lst_sth = []
    for _ in range(width):
        lst_sth.append(0)

    for _ in range(deep):
        floor = input()
        lst_floor = floor.split()
        for j in range(len(lst_floor)):
            lst_ansth = lst_sth
            lst_sth[j] = lst_ansth[j] + float(lst_floor[j])
    print('%d' %max(lst_sth))
main(int(input()), int(input()))
