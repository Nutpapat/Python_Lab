#NUTPAPAT YOUYOUNG 60070024
"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """This is Show Program Check A sequence number three ascending and descending"""
    choose = input()
    number_1 = (float(input()))
    number_2 = (float(input()))
    number_3 = (float(input()))
    if:
        if number_1 < number_2 or number_1 < number_3:
            return number_1
        elif number_2 < number_1 or number_2 < number_3:
            return number_2
        elif number_3 < number_1 or number_3 < number_2:
            return number_3
    elif choose == "Ascend":
        print("%.2f," %number_1, "%.2f," %number_2, "%.2f" %number_3)
    
    if choose == "Descend":
        print("%.2f," %number_1, "%.2f," %number_2, "%.2f" %number_3)

def chk(Ascend):
    """Check"""
    
main()
