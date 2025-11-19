from lab9_func import sqr_int_matrix_input

matrix = sqr_int_matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()

print("\nИсходная матрица:")
for row_indx in range(len(matrix)):
    row_to_print = " "

    for indx_in_row in range(len(matrix[0])):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < len(matrix) - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        
    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

matrix_len = len(matrix)
for i in range(matrix_len // 2):
    for j in range(i, matrix_len - 1 - i):
        temporary = matrix[i][j]
        matrix[i][j] = matrix[matrix_len - 1 - j][i]
        matrix[matrix_len - 1 - j][i] = matrix[matrix_len - 1 - i][matrix_len - 1 - j]
        matrix[matrix_len - 1 - i][matrix_len - 1 - j] = matrix[j][matrix_len - 1 - i]
        matrix[j][matrix_len - 1 - i] = temporary

print("\nНовая матрица после поворота по часовой:")
for row_indx in range(len(matrix)):
    row_to_print = " "

    for indx_in_row in range(len(matrix[0])):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < len(matrix) - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        
    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

for i in range(matrix_len // 2):
    for j in range(i, matrix_len - 1 - i):
        temporary = matrix[i][j]
        matrix[i][j] = matrix[j][matrix_len - 1 - i]
        matrix[j][matrix_len - 1 - i] = matrix[matrix_len - 1 - i][matrix_len - 1 - j]
        matrix[matrix_len - 1 - i][matrix_len - 1 - j] = matrix[matrix_len - 1 - j][i]
        matrix[matrix_len - 1 - j][i] = temporary

print("\nНовая матрица после поворота по часовой:")
for row_indx in range(len(matrix)):
    row_to_print = " "

    for indx_in_row in range(len(matrix[0])):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < len(matrix) - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        
    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)