"""
PSIT Pair Programming
#1 - Teerapat Kraisrisirikul (60070183)
#2 - Sopoat Iamcharoen (60070101)
"""
 
def main():
    """Main fuction"""
    side_1, side_2, side_3 = order_ascend(float(input()), float(input()), float(input()))
    triangle = side_3**2-0.01 <= side_1**2 + side_2**2 <= side_3**2+0.01
    if triangle:
        print("Yes")
    else:
        print("No")
 
def order_ascend(num1, num2, num3):
    """Order numbers from low to high"""
    if num1 > num2:
        num1, num2 = swap(num1, num2)
    if num2 > num3:
        num2, num3 = swap(num2, num3)
    if num1 > num2:
        num1, num2 = swap(num1, num2)
    return num1, num2, num3
 
def swap(num_a, num_b):
    """Swap the values"""
    return num_b, num_a
 
main()