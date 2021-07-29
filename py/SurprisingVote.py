"""SurprisingVote"""
def main(mark3, markh):
    """func"""
    if 0 <= markh <= 10 and mark3 >= markh:
        mark_new = (mark3-markh)//2
        if markh - mark_new == 2 and mark_new > 0:
            mark_new -= 1
        if markh - mark_new > 2:
            print("Surprising")
        else:
            print("Not surprising")
main(float(input()), float(input()))
