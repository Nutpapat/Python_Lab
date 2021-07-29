#NUTPAPAT YOUYOUNG 60070024
"""Pressurize"""
def main():
    """This is Show Program Compare Pressurize"""
    inside = float(input())
    outside = float(input())
    answer = abs(inside - outside)
    answer1 = answer/inside
    answer2 = answer1*100
    if outside < inside:
        if answer2 > 30:
            print("Underpressure %.4f" %answer2+"%")
        else:
            print("Safe %.4f" %answer2+"%")
    if outside > inside:
        if answer2 > 30:
            print("Overpressure %.4f" %answer2+"%")
        else:
            print("Safe %.4f" %answer2+"%")
main()
