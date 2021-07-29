"""
PSIT Midterm Examination (Rerun) - Sequence XXX
Teerapat Kraisrisirikul (60070183)
"""
 
def main(size, num):
    """ Main function """
    #Spacing variables
    side = 0
    center = size-4
 
    #Upper borders
    print(("*" * size + " ") * num)
 
    #Upper lines
    for _ in range((size-3)//2):
        print(("*" + " "*side + "*" + " "*center + "*" + " "*side + "* ") * num)
        side += 1
        center -= 2
 
    #Middle line
    if size > 1:
        print(("*" + " "*side + "*" + " "*side + "* ") * num)
 
    #Lower lines
    for _ in range((size-3)//2):
        side -= 1
        center += 2
        print(("*" + " "*side + "*" + " "*center + "*" + " "*side + "* ") * num)
 
    #Lower borders
    if size > 1:
        print(("*" * size + " ") * num)
 
main(int(input()), int(input()))