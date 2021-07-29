"""Matrix_"""
def matrix(var1, var2, lst_tmp, lst):
    """Make Maxtrix_[[], []]_"""
    for _ in range(var1):
        lst_tmp = []
        for _ in range(var2):
            lst_tmp.append(int(input()))
        lst.append(lst_tmp)
    return lst

def main(var_p, var_q, var_r, resu):
    """fn_"""
    matrix_a = matrix(var_p, var_q, [], [])
    matrix_b = matrix(var_q, var_r, [], [])
    for i in range(var_p):
        for j in range(var_r):
            resu = [matrix_a[i][k] * matrix_b[k][j] for k in range(var_q)]
            print(sum(resu), end=' ')
        print()
main(int(input()), int(input()), int(input()), 0)
