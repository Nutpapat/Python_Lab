"""050: TheFlood I"""
def main():
    """water flood"""
    count = 0
    barier = input().split()
    barier = [int(i) for i in barier]
    if 0 in barier:
        return print(0)
    while True:
        barier.sort()
        count += 1
        for i in range(1, len(barier)):
            barier[i] = barier[i]-1
        if 0 in barier:
            break
    print(count)
main()
