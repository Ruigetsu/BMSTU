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


matrix = [list(row[::-1]) for row in list(zip(*matrix))]
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

matrix = [list(row) for row in reversed(list(zip(*matrix)))]

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