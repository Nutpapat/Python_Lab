"""Turnstile"""
def main():
    """This is show program Turnstile"""
    state = 1
    count = 0
    while True:
        turn = input()
        if turn == "END":
            print(count)
            break
        if state == 1 and turn == "C":
            state = 0
            continue
        if state == 1 and turn == "P":
            continue
        if state == 0 and turn == "C":
            continue
        if state == 0 and turn == "P":
            count += 1
            state = 1
main()
