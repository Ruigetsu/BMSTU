from lab9_func import check

A = []
nums = input("Введите значения для массива А через пробел: ").split()
for num in nums:
    if num == '':
        continue
    else:
        if check(num) is False:
            print('Вы ввели некорректное значение')
            exit()
        else:
            A.append(check(num))

B = []
nums = input("Введите значения для массива B через пробел: ").split()
for num in nums:
    if num == '':
        continue
    else:
        if check(num) is False:
            print('Вы ввели некорректное значение')
            exit()
        else:
            B.append(check(num))


matrix = [[a*b for b in B] for a in A]

for row_indx in range(len(A)):
    squares = 0
    for indx_in_row in range(len(B)):
        num = B[indx_in_row]*A[row_indx]
        if num**0.5 == int(num**0.5):
            squares += 1
    matrix[row_indx].append(squares)



print("\nНовая матрица:")
for row_indx in range(len(matrix)):
    row_to_print = ''
    for indx_in_row in range(len(matrix[row_indx]) - 1):
        row_to_print += f'{matrix[row_indx][indx_in_row]:^4}'
    row_to_print += f"| {matrix[row_indx][-1]:^4}"
    print(row_to_print)



