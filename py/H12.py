"""ShowbyRock"""
def main():
    """ShowbyRock"""
    play1 = input()
    play2 = input()
    if play1 == "Rock" and play2 == "Scissors":
        print("God of Banana")
        print("Rock!!!")
    elif play1 == "Scissors" and play2 == "Paper":
        print("God of Banana")
    elif play1 == "Paper" and play2 == "Rock":
        print("God of Banana")
    elif play1 == "Rock" and play2 == "Paper":
        print("Banabird")
        print("Rock!!!")
    elif play1 == "Scissors" and play2 == "Rock":
        print("Banabird")
    elif play1 == "Paper" and play2 == "Scissors":
        print("Banabird")
    elif play1 == "Rock" and play2 == "Rock":
        print("Banabana")
        print("Rock!!!")
    else:
        print("Banabana")
main()
