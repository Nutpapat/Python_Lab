"""
PSIT - Week 12
Teerapat Kraisrisirikul (60070183)
"""
 
import json
 
def main():
    """ Main function """
    list_a, list_b = json.loads(input()), json.loads(input())
    target = int(input())
    list_a, list_b = [i for i in list_a if i <= target], [i for i in list_b if i <= target]
    print(sum([list_a.count(target-i) for i in list_b]))
 
main()