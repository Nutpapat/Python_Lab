"""029"""
def main():
    """Triathlon"""
    num = int(input())
    swim = 0
    cycling = 0
    run = 0
    for _ in range(num):
        swim2 = float(input())
        cycling2 = float(input())
        run2 = float(input())
        for _ in range(25600):
            swim += swim2
        for _ in range(746):
            cycling += cycling2
        for _ in range(2122):
            run += run2
        ans = swim + cycling + run
        print("%.02f"%ans)
        swim = 0
        cycling = 0
        run = 0
main()
