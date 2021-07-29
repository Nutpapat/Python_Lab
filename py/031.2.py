"""031"""
def main():
    """031"""
    num = int(input())
    count = 1
    for _ in range(num):
        if count != 1:
            for i in range(1, count):
                print(i, end=" ")
        print(count)
        count += 1
    count = num-1
    for _ in range(num):
        for i in range(1, count):
            print(i, end=" ")
        print(count)
        count -= 1
        if count == 0:
            break
main()
