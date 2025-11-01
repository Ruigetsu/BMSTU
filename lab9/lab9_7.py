from lab9_func import matrix_input

massive = []
x = None 
y = None
while True: 
    curr_matrix = matrix_input()
    if curr_matrix is False:
        break
    if x == None: 
        x = len(curr_matrix)
        y = len(curr_matrix[0])
    elif len(curr_matrix) != x or len(curr_matrix[0]) != y:
        print("Размер матрицы некоректный")
        continue
    massive.append(curr_matrix)
z = len(massive)

max_dimension = max(x,y,z)
slice_indx = max_dimension//2

for matrix_indx in range(z):
    print(f"\nМатрица {matrix_indx+1}")
    for row_indx in range(x):
        row_to_print = '|'
        for indx_in_row in range(y):
            row_to_print += f'{massive[matrix_indx][row_indx][indx_in_row]:^10g}|'
        print(row_to_print)
        if row_indx != x - 1:
            print("-"*len(row_to_print))


if max_dimension == z:
    print(f"\nСрез по матрице с индексом {slice_indx}") 
    for row in massive[slice_indx]:
        row_to_print = '|'
        for num in row:
            row_to_print += f'{num:^10g}|'
        print(row_to_print)

elif max_dimension == x:
    print(f"\nСрез по строке с индексом {slice_indx}") 
    for matrix_indx in range(z):
        row_to_print = '|'
        for row in massive[matrix_indx][slice_indx]:
            row_to_print += f'{row:^10g}|'
        print(row_to_print)
    
else:
    print(f"\nСрез по столбцу с индексом {slice_indx}") 
    for matrix_indx in range(z):
        row_to_print = "|"
        for row in massive[matrix_indx]:
            row_to_print += f'{row[slice_indx]:^10g}|'
        print(row_to_print)