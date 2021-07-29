"""
PSIT - Week 12
Teerapat Kraisrisirikul (60070183)
"""
 
def main():
    """ Main function """
    gates = sorted([int(i) for i in input().split()])
    days = 0
 
    if gates[0] < gates[1] and min(gates) > 0:
        days += gates[1]-gates[0]
        gates = [gates[0]] + [gates[i]-(gates[1]-gates[0]) for i in range(1, len(gates))]
 
    while (0 in gates) == False:
        gates = sorted(gates)
        gates = [gates[0]] + [gates[i]-1 for i in range(1, len(gates))]
        days += 1
 
    print(days)
 
main()