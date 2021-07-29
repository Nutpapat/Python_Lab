"""60070001 & 60070008"""
def main(width, row):
    """scaledmatrix"""
    total = []
    total_2 = []
    total_3 = []
    count = 0
    for _ in range(width*row):
        number = float(input())
        total.append(number)
    total_min = min(total)
    for i in total:
        total_2.append(i-total_min)
    total_max = max(total_2)
    for j in total_2:
        total_3.append(j/total_max)
    for k in total_3:
        print("%.2f" %k, end=" ")
        count += 1
        if count == row:
            print()
            count = 0
main(int(input()), int(input()))
