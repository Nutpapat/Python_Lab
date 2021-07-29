"""60070001 & 60070008"""
def main(number, answer):
    """Dart"""
    for _ in range(number):
        var_x, var_y = input().split()
        check = (int(var_x)**2+int(var_y)**2)**0.5
        answer += [5 if check <= 2 else 4 if check <= 4 else 3 if check <= 6 else 2 if check <= 8 \
        else 1 if check <= 10 else 0]
    print(sum(answer))
main(int(input()), [])
