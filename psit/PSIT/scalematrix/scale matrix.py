"""ScaledMatrix"""
def scaled_matrix(row, column):
    """Print matrix that value is between 0 - 1."""
    list_value = []
    list_scled = []
    count = 0
    for _ in range(row):
        for _ in range(column):
            value = float(input())
            list_value.append(value)
    max_value = max(list_value)
    min_value = min(list_value)
    for val in list_value:
        scaled = (val - min_value)/(max_value - min_value)
        list_scled.append(scaled)
    for scale in range(len(list_scled)):
        print("%.2f"%list_scled[scale], end=" ")
        count += 1
        if count == column:
            print()
            count = 0
scaled_matrix(int(input()), int(input()))
