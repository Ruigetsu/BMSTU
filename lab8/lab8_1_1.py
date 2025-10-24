from lab8_func import matrix_input
matrix = matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()

indx_of_max_avg = -1
max_avg = float("-inf")
matrix_width = len(matrix[0])
print("\nИзначальная матрица:")
for row_indx in range(len(matrix)):
    s = 0

    row_to_print = " " 

    for indx_in_row in range(matrix_width):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < matrix_width - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"

        s += num

    avg = s/matrix_width
    if avg > max_avg:
        max_avg = avg
        indx_of_max_avg = row_indx
    if row_indx < len(matrix) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

print(f"\nНаибольшее среднее арифмитическое имеет строка {indx_of_max_avg+1} = {max_avg}")