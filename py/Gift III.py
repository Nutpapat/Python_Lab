"""Gift III"""
def main():
    """This is show program to think of inflation"""
    gift = int(input())
    chk_1 = 0
    chk_2 = 0
    for _ in range(gift):
        gift_x = int(input())
        if gift_x > chk_1:
            chk_2 = chk_1
            chk_1 = gift_x
        else:
            if gift_x > chk_2 and gift_x < chk_1:
                chk_2 = gift_x
    if gift == 1:
        print("Exit")
    elif chk_2 == 0:
        print("Exit")
    elif chk_1 == chk_2:
        print("Exit")
    else:
        print(chk_2)
main()
