"""Circular II"""
def main(me_x, me_y, me_r, it_x, it_y):
    """func"""
    it_r = float(input())
    dist = ((me_x-it_x)**2 + (me_y-it_y)**2)**0.5
    if dist >= me_r + it_r:
        print("No")
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
