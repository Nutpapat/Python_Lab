"""Filter"""
import json
def main():
    """Print student id and score"""
    dct = json.loads(input())
    score = float(input())
    lst_id = []
    lst_score = []
    for keys in dct:
        lst_id.append(keys)
    lst_id_sort = sorted(lst_id)
    for i in lst_id_sort:
        ans = dct[i]
        if ans >= score:
            lst_score.append(ans)
            print("%s\t%.2f" %(i, ans))
    if lst_score == []:
        print("Nope")
main()
