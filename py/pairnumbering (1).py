"""60070001 & 60070008"""
import json
def main():
    """PairNumbering"""
    list_a = sorted(json.loads(input()))
    list_b = json.loads(input())
    number = int(input())
    check = []
    count = 0
    for i in list_a:
        if i not in check:
            if i <= number:
                count += (list_b.count(number-i)*list_a.count(i))
                check.append(i)
            else:
                break
    print(count)
main()
