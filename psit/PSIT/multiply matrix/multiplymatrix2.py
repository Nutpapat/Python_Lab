"""Multiply matrix_Problem."""
def find_matrix(row1, column1):
    """return matrix"""
    lis = []
    lis2 = []
    check = 0
    for _ in range(row1*column1):
        lis2.append(int(input()))
        diff = column1-1
        if check == diff:
            lis.append(lis2)
            lis2, check = [], 0
            continue
        check = check+1
    return lis

def multiply_matrix(matrix1, matrix2, one, two, multiply=0):
    """return multiply"""
    for i in range(len(matrix2)):
        multiply = multiply + matrix1[one][i]*matrix2[i][two]#result sum matrix
    return multiply

def result_matrix(row2, column3, column2):
    """print multiply matrix"""
    matrix1 = find_matrix(row2, column3)
    matrix2 = find_matrix(column3, column2)
    for i in range(row2):
        for j in range(column2):
            answer = multiply_matrix(matrix1, matrix2, i, j)
            if j == column2-1:
                print(answer)
            else:
                print(answer, end=" ")

result_matrix(int(input()), int(input()), int(input()))
