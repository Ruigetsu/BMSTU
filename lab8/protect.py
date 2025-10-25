from lab8_func import matrix_input
matrix = matrix_input()
if matrix == False: 
    print("Вы ничего не ввели")
    exit()
elements = []
matrix_width = len(matrix[0])
matrix_height = len(matrix)
print("\nИзначальная матрица:")
for row_indx in range(matrix_height):
    row_to_print = " "
    for indx_in_row in range(matrix_width):
        num = matrix[row_indx][indx_in_row]
        if indx_in_row < matrix_height - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        elements.append(num)
    if row_indx < matrix_height - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

for i in range(1,len(elements)):
    curr = elements[i]
    pos = i - 1
    while pos >= 0 and elements[pos] > curr:
        elements[pos+1] = elements[pos]
        pos -= 1
    elements[pos+1] = curr

size_matrix = matrix_width*matrix_height
k = 0
row_indx = 0
indx_in_row = 0
direction = "right"
left_border = 0
up_border = 1
while k <= size_matrix - 1:
    if direction == "right":
        matrix[row_indx][indx_in_row] = elements[k]
        if indx_in_row == matrix_width - 1:
            direction = "down"
            matrix_width -= 1
            row_indx += 1
        else:
            indx_in_row += 1
    elif direction == "down":
        matrix[row_indx][indx_in_row] = elements[k]
        if row_indx == matrix_height - 1:
            direction = "left"
            matrix_height -= 1
            indx_in_row -= 1
        else:
            row_indx += 1
    elif direction == "left":
        matrix[row_indx][indx_in_row] = elements[k]
        if indx_in_row == left_border:
            direction = "up"
            left_border += 1
            row_indx -= 1
        else:
            indx_in_row -= 1
    else:
        matrix[row_indx][indx_in_row] = elements[k]
        if row_indx == up_border:
            direction = "right"
            up_border += 1
            indx_in_row += 1
        else:
            row_indx -= 1
    k += 1

print("\nНовая матрица:")
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