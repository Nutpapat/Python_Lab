"""Grade II"""
def calculate():
    """This is show program calculate grade"""
    score = float(input())
    if 95 < score and score <= 100:
        print("A")
    elif 90 < score and score < 95:
        print("B+")
    elif 85 < score and score < 90:
        print("B")
    elif 80 < score and score < 85:
        print("C+")
    elif 75 < score and score < 80:
        print("C")
    elif 70 < score and score < 75:
        print("D+")
    elif 65 < score and score < 70:
        print("D")
    elif 60 < score and score < 65:
        print("F+")
    elif 0 < score and score < 60:
        print("F")
    elif 0 > score or score > 100:
        print("ERR")
calculate()
