"""
PSIT - Week 10
Teerapat Kraisrisirikul (60070183)
"""
 
def main():
    """ Main function """
    group_a_amt, group_b_amt = int(input()), int(input())
    group_a, group_b = [input() for _ in range(group_a_amt)], [input() for _ in range(group_b_amt)]
 
    shared = [i for i in group_a if i in group_b]
    print("Nope" if len(shared) == 0 else "\n".join(sorted([i for i in shared], reverse=True)))
 
main()