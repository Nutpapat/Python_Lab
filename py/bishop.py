"""047: BishopMove"""
def show(bi_x, bi_y, en_x, en_y):
    """This function that show BishopMove"""
    check = int(input())
    enx = int(input())
    eny = int(input())
    way_x = bi_x-enx
    way_y = bi_y-eny
    if abs(way_x) == abs(way_y):
        if way_x >= 0 and way_y >= 0: #+,+
            return 1, way_x, bi_x, bi_y, en_x, en_y, check, enx, eny
        if way_x > 0 and way_y < 0: #+,-
            return 2, way_x, bi_x, bi_y, en_x, en_y, check, enx, eny
        if way_x < 0 and way_y < 0: #-,-
            return 3, way_x, bi_x, bi_y, en_x, en_y, check, enx, eny
        if way_x < 0 and way_y > 0: #-,+
            return 4, way_x, bi_x, bi_y, en_x, en_y, check, enx, eny
    return 0, way_x, bi_x, bi_y, en_x, en_y, check, enx, eny

def bishop(ta_x, ta_y):
    """This function that check way of bishop"""
    count, way_x, bi_x, bi_y, en_x, en_y, check, enx, eny = (show(int(input()), int(input()),\
    int(input()), int(input())))
    dex = bi_x-en_x
    if bi_x > ta_x and bi_y > ta_y:
        print("No")
    if count == 0:
        print("No")
    else:
        count2 = enemy(en_x, en_y, bi_x, bi_y)
        if en_y == eny and en_x == enx and count2 == count:
            if check == 1:
                print("Yes")
            else:
                print("No")
        elif count2 == count:
            if abs(dex) < abs(way_x):
                print("No")
            else:
                print("Yes")
        else:
            print("Yes")

def enemy(en_x, en_y, bi_x, bi_y):
    """This function that check way of enemy"""
    dex = bi_x-en_x
    dey = bi_y-en_y
    if abs(dex) == abs(dey):
        if dex > 0 and dey > 0: #+,+
            return 1
        if dex > 0 and dey < 0: #+,-
            return 2
        if dex < 0 and dey < 0: #-,-
            return 3
        if dex < 0 and dey > 0: #-,+
            return 4
    return 0

bishop(int(input()), int(input()))
