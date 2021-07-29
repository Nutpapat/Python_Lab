"""RockPaperScissor"""
def calculate_rps(check, score_a, score_b):
    """-"""
    if check == 'RP' or check == 'SR' or check == 'PS':
        score_b += 1
    elif check == 'PR' or check == 'RS' or check == 'SP':
        score_a += 1
    return score_a, score_b
 
def show_rps(word, score_a, score_b):
    """-"""
    for alpha in range(0, len(word), 2):
        check = (word[alpha]+word[alpha+1])
        score_a, score_b = calculate_rps(check, score_a, score_b)
    if score_a > score_b:
        print("A win "+str(score_a)+"-"+str(score_b))
    elif score_b > score_a:
        print("B win "+str(score_b)+"-"+str(score_a))
    elif score_b == score_a:
        print("DRAW "+str(score_a))
show_rps(input(), 0, 0)
