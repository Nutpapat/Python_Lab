"""
PSIT Pair-Programming (21/Sep/2017)
#1 - Teerapat Kraisrisirikul (60070183)
#2 - Siwakorn Lertamnuaylap (60070095)
"""
 
def main():
    """ Main function """
    secs, mins, hrs, days = int(input()), int(input()), int(input()), int(input())
    hrs_final = str((secs//mins//hrs)%days)
    mins_final = str((secs//mins)%hrs)
    secs_final = str(secs%mins)
    print(hrs_final + ":" + mins_final + ":" + secs_final)
 
main()