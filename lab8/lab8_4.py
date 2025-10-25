from lab8_func import matrix_input
matrix = matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()

indx_max_sum = 0
indx_min_sum = 0
max_sum = float("-inf")
min_sum = float("inf")

matrix_width = len(matrix[0])

print("\nИзначальная матрица:")
for row_indx in range(len(matrix)):
    row_to_print = " "

    for indx_in_row in range(matrix_width):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < matrix_width - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        
    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

for indx_in_row in range(matrix_width):
    s = 0

    for row_indx in range(len(matrix)):
        s += matrix[row_indx][indx_in_row]

    if s > max_sum:
        max_sum = s
        indx_max_sum = indx_in_row
    elif s < min_sum:
        min_sum = s
        indx_min_sum = indx_in_row

for row_indx in range(len(matrix)):
    matrix[row_indx][indx_max_sum], matrix[row_indx][indx_min_sum] = matrix[row_indx][indx_min_sum], matrix[row_indx][indx_max_sum]

print("\nНовая матрица:")
for row_indx in range(len(matrix)):
    row_to_print = " "

    for indx_in_row in range(matrix_width):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < matrix_width - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        
    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)