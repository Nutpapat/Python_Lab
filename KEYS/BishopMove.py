"""
PSIT - Week 13
Teerapat Kraisrisirikul (60070183)
"""
 
def main():
    """ Main function """
    board = int(input()), int(input())
    bishop = int(input()), int(input())
    other = int(input()), int(input())
    is_enemy = int(input())
    target = int(input()), int(input())
    print(progress(board, bishop, other, is_enemy, target))
 
def progress(board, bishop, other, is_enemy, target):
    """ Progress of checking """
    if target == bishop:
        return 'Yes'
    # Target is anywhere, except the bishop coordinates.
    if in_path(bishop, target) == False:
        return 'No'
    # Target is now in path.
    if in_path(bishop, other) == False:
        return 'Yes'
    # Both target and other is now in path
    if (other == target) and is_enemy:
        return 'Yes'
    if (other == target) and is_enemy == 0:
        return 'No'
    # Other is not on the target
    if not_blocked(board, bishop, other, target):
        return 'Yes'
    # Path is now blocked
    return 'No'
 
def in_path(bishop, obj):
    """ Check if the target is in path """
    return abs(bishop[0]-obj[0]) == abs(bishop[1]-obj[1])
 
def not_blocked(board, bishop, other, target):
    """ Check if the path is blocked by another chess """
    walk_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
 
    for i in walk_directions:
        area = bishop
        pass_obj = False
        while True:
            area = area[0] + i[0], area[1] + i[1]
            if (0 <= area[0] < board[0]) == False or (0 <= area[1] < board[1]) == False:
                break
            elif area == target:
                if pass_obj:
                    return False
                pass_obj = True
            elif area == other:
                if pass_obj:
                    return True
                pass_obj = True
    return True
 
main()