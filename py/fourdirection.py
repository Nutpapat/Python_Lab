"""60070001 & 60070008"""
def main(text):
    """fourdirection"""
    word_u = ["  *  ", " *** ", "* * *", "  *  ", "  *  "]
    word_d = ["  *  ", "  *  ", "* * *", " *** ", "  *  "]
    word_l = ["  *  ", " *   ", "*****", " *   ", "  *  "]
    word_r = ["  *  ", "   * ", "*****", "   * ", "  *  "]
    for i in range(5):
        for j in text:
            if j == "U":
                print(word_u[i], end=" ")
            elif j == "D":
                print(word_d[i], end=" ")
            elif j == "L":
                print(word_l[i], end=" ")
            elif j == "R":
                print(word_r[i], end=" ")
        print()
main(input().upper())
