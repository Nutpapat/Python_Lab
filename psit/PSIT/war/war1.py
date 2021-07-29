"""WarLab"""
import json
def who_is_winner(atkk, deff):
    """ print summary of winner """
    ans = 0
    atkk.sort(reverse=True)
    deff.sort(reverse=True)
    for i in deff:
        for j in atkk:
            if j > i:
                ans += j
                atkk.remove(j)
            break
    print(ans)
who_is_winner(json.loads(input()), json.loads(input()))
