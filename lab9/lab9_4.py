from lab9_func import matrix_input,check_int

D = matrix_input()
if D == False:
    print("Вы ввели пустую матрицу")
    exit()

I = set()
print("Введите элемента массива I")
while True:
    inp = input()
    if len(inp) == 0:
        break
    num = check_int(inp)
    if check_int(inp) is False or num < 1 or num > len(D):
        print("Вы ввели некорректное число")
    else:
        I.add(num)
I = list(I)
R = []
for row_indx in I:
    max_num = -float("inf")
    for indx_in_row in range(len(D[0])):
        max_num = max(max_num,D[row_indx-1][indx_in_row])
    R.append(max_num)
avg = sum(R)/len(R)

print("\nМатрица D:")
for row_indx in range(len(D)):
    row_to_print = " "

    for indx_in_row in range(len(D[0])):
        num = D[row_indx][indx_in_row]
        if indx_in_row < len(D) - 1:
            row_to_print += f"{num:^10g}|"
        else: 
            row_to_print += f"{num:^10g}"
        
    if row_indx < len(D) - 1:
        print(row_to_print)
        print("-"*(len(row_to_print)))
    else:
        print(row_to_print)

print(f"\nМассив I = {I}\n\
Массив R = {R}\n\
Среднее ариф. = {avg}")
