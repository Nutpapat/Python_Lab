"""
PSIT Midterm Examination (Rerun) - Donut
Teerapat Kraisrisirikul (60070183)
"""
 
def main():
    """ Main function """
    price, amount, free, demand = int(input()), int(input()), int(input()), int(input())
    demand_pack = demand//(amount+free) #Demanded packages of donut.
    demand %= (amount+free)             #Demanded extra donuts.
 
    #Calculating on extra donuts
    if demand < amount:
        #Demand is less than the promotion amount.
        pay = demand * price
        get = demand
    elif demand >= amount:
        #Demand reaches the promotion amount.
        pay = amount * price
        get = amount+free
 
    #Calculating on donut packages
    pay += demand_pack * amount * price
    get += demand_pack * (amount+free)
 
    #Output
    print(pay, get)
 
main()