"""Circular I"""
def main(me_x, me_y, me_r, it_x, it_y):
    """func"""
    dist = ((me_x-it_x)**2 + (me_y-it_y)**2)**0.5
    if dist <= me_r:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
