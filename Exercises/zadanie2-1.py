n = int(input("Введите номер члена послед. Фибоначчи, где первый член - 1, а второй - 1: "))
Fibonachi1 = 1
prev_num = 1

if n == 1 or n == 2: 
    if n == 1: 
        print(f"{n}-й член = {Fibonachi1}")
    else: 
        print(f"{n}-й член = {prev_num}")

i = 2
num = Fibonachi1 + prev_num
while i < n - 1: 
    num, prev_num= num + prev_num, num
    i += 1
print(f"{n}-й член = {num}")

