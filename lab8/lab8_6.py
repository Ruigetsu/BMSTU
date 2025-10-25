from lab8_func import matrix_input
matrix = matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()


max_num_over_first = float("-inf") #Максимальное значение над главной диагональю
min_num_under_second = float("inf") #Минимальное значение под побочной диагональю
print("\nИзначальная матрица:")
for row_indx in range(len(matrix)):
    row_to_print = " "
    for indx_in_row in range(len(matrix)):
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

for row_indx in range(len(matrix)):
    indx_first_diag = row_indx #Индекс элемента на главной диагонали

    for indx_in_row in range(row_indx+1,len(matrix)):
        matrix[row_indx][indx_in_row], matrix[indx_in_row][row_indx] = matrix[indx_in_row][row_indx], matrix[row_indx][indx_in_row]

print("\nНовая матрица:")
for row_indx in range(len(matrix)):
    row_to_print = " "

    for indx_in_row in range(len(matrix)):
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
        

    