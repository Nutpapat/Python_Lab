"""Classify"""
def main():
    """score"""
    dic = {}
    while True:
        tmp = input()
        if tmp == 'END':
            break
        year = tmp[:2]
        faculty = int(tmp[2:4])
        if year not in dic:
            dic.setdefault(year, {faculty:1})
        else:
            if faculty not in dic[year]:
                dic[year][faculty] = 1
            else:
                dic[year][faculty] += 1
    for i in sorted(dic):
        chk = 1
        for j in sorted(dic[i]):
            if chk == 1:
                chk = 0
                print(i, j, dic[i][j])
            else:
                print('--', j, dic[i][j])
main()
