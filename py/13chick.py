"""Week 11 - 60070024 && 60070031"""
def main(wei_box, wei_chick):
    """ FoodGrade II """
    lst_weight = wei_chick.split()
    lst_int_input = []
    for i in lst_weight:
        lst_int_input.append(float(i))
    lst_int_input.sort()

    total_wei = 0
    count_box = 0
    for i in range(len(lst_int_input)):
        if total_wei < wei_box:
            total_wei += lst_int_input[i]
            count_box += 1

            continue
        elif total_wei == wei_box:
            break
    if total_wei > wei_box:
        count_box -= 1
    print(count_box)
main(int(input()), input())
