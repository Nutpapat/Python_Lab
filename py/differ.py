"""Difference"""
def main():
    """Difference"""
    num_n = int(input())
    num_m = int(input())
    lst_n = []
    lst_m = []
    lst_ans = []
    for _ in range(num_n):
        lst_n.append(int(input()))
    for _ in range(num_m):
        lst_m.append(int(input()))
    for i in lst_n:
        if i not in lst_m:
            lst_ans.append(str(i))
    print(" ".join(lst_ans))
main()
