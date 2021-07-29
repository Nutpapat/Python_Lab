"""island"""
def main(island):
    """output"""
    island_row, island_col = [int(x) for x in input().split()]
    lst_island = [input().split() for _ in range(island_row)]
    for row in range(island_row):
        for col in range(island_col):
            if lst_island[row][col] == '1':
                island += 1
                lst_island = same_island(col, row, lst_island)
    print(island)

def same_island(col, row, lst_island):
    """find same island"""
    surround = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), \
            (row, col), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
    for i, j in surround:
        if i < 0 or j < 0 or i > len(lst_island)-1 or j > len(lst_island[0])-1:
            pass
        elif lst_island[i][j] == '1':
            lst_island[i][j] = '2'
            lst_island = same_island(j, i, lst_island)
    return lst_island
main(0)
