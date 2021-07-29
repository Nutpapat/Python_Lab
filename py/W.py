#NUTPAPAT YOUYOUNG 60070024
"""WeightStation"""
def check():
    """This is Show Program Check truck weight"""
    avr_wg = float(input())
    wg_1 = float(input())
    wg_2 = float(input())
    wg_3 = float(input())
    lost_wg = (avr_wg*4) - (wg_1 + wg_2 + wg_3)
    sum_wg = wg_1 + wg_2 + wg_3 + lost_wg
    if sum_wg >= 15000:
        print("Overweight")
    else:
        if abs(wg_1 - avr_wg) > avr_wg/2:
            print("Unbalance")
        elif  abs(wg_2 - avr_wg) > avr_wg/2:
            print("Unbalance")
        elif  abs(wg_3 - avr_wg) > avr_wg/2:
            print("Unbalance")
        elif abs(lost_wg - avr_wg) > avr_wg/2:
            print("Unbalance")
        else:
            print("Pass %.2f"%(lost_wg))
check()
