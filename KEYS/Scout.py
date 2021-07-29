"""
PSIT - Week 14
Teerapat Kraisrisirikul (60070183)
"""
 
def main():
    """ Main function """
    for _ in range(int(input())):
        data = tuple([int(i) for i in input().split()])
        eggs = sorted([int(i) for i in input().split()])
 
        pot = {'amount': 0, 'weight': 0}
 
        for i in range(data[0]):
            if (eggs[i] <= data[2]-pot['weight']) and (pot['amount'] < data[1]):
                pot['amount'] += 1
                pot['weight'] += eggs[i]
 
        print(pot['amount'])
 
main()