"""EuclideanDistance Problem"""
def euclideandistance(roundnumber, dsitance):
    """Find dsitance from the begin to end"""
    list_point = []
    for _ in range(roundnumber):
        point = input().split(" ")
        point = [int(point[0]), int(point[1])]
        list_point.append(point)
        print(list_point)
        if len(list_point) == 2:
            dsitance += ((list_point[0][0]-list_point[1][0])**2\
                +(list_point[0][1]-list_point[1][1])**2)**0.5
            list_point.pop(0)
    print("%.2f" %dsitance)

euclideandistance(int(input()), 0)
