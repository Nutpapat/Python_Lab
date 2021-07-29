"""
PSIT - Week 11
Teerapat Kraisrisirikul (60070183)
"""
 
def main():
    """ Main function """
    groups = int(input())
    coordinates = [[] for _ in range(groups)]
 
    for i in range(groups):
        for _ in range(int(input())):
            data = input()
            data += " " + str(sum([int(i) for i in data.split()]))
            coordinates[i].append(tuple([int(i) for i in data.split()[-1::-1]]))
        coordinates[i].sort()
        coordinates[i] = coordinates_sort(coordinates[i])
        _ = [print(j[2], j[1]) for j in coordinates[i]]
 
def coordinates_sort(coordinates):
    """ Sort the coordinates """
    coordinates_pre = list()
    saved = list()
    point_saved = None
    for i in coordinates:
        if i[0] != point_saved:
            for j in sorted(saved, reverse=True):
                coordinates_pre.append(j)
            saved = []
            saved.append(i)
        elif i[0] == point_saved:
            saved.append(i)
        point_saved = i[0]
 
    for j in sorted(saved, reverse=True):
        coordinates_pre.append(j)
    return coordinates_pre
 
main()