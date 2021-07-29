""" Week 11 - 60070024 && 60070031 """
def main(piece, food):
    """ Refrigerator """
    piece = food.split()
    for i in range(len(piece)):
        piece[i] = int(piece[i])
    count_day = 0
    while True:
        piece.sort()
        for i in range(1, len(piece)):
            piece[i] = piece[i]-1
        count_day += 1
        if 0 in piece:
            break
    print(count_day)
main(int(input()), input())
