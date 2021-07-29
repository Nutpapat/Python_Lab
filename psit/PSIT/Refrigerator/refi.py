"""Refrigerator"""
def check_day(data_num, num):
    """print day of stock food longest"""
    day = 0
    if len(data_num) != num:
        print("0")
    else:
        while 1 == 1:
            if min(data_num) == 0:
                print(day)
                break
            else:
                stock = min(data_num)
                data_num.remove(stock)
            for i in range(len(data_num)):
                data_num[i] = data_num[i]-1
            day += 1
            data_num.append(stock)

def data_refi(num):
    """put data of food and day to expire of food"""
    data_num = []
    data_raw = input()
    data = ""
    for i in range(len(data_raw)):
        if data_raw[i] == " ":
            data_num.append(int(data))
            data = ""
        elif i+1 == len(data_raw):
            data += data_raw[i]
            data_num.append(int(data))
        else:
            data += data_raw[i]
    check_day(data_num, num)
data_refi(int(input()))
