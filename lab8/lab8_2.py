from lab8_func import matrix_input
matrix = matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()

indx_count_max_negative = 0
indx_count_min_negative = 0
max_count = 0
min_count = float("inf")

matrix_width = len(matrix[0])
print("\nИзначальная матрица:")
for row_indx in range(len(matrix)):
    count_negative = 0
    row_to_print = " " 

    for indx_in_row in range(matrix_width):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < matrix_width - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"

        if num < 0: 
            count_negative += 1

    if count_negative > max_count:
        max_count = count_negative
        indx_count_max_negative = row_indx
    elif count_negative < min_count:
        min_count = count_negative
        indx_count_min_negative = row_indx

    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

matrix[indx_count_max_negative], matrix[indx_count_min_negative] = matrix[indx_count_min_negative], matrix[indx_count_max_negative]

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