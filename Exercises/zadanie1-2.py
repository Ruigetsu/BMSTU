list_of_num = []
while True:
    x = int(input())
    if x == 0:
        break 
    list_of_num.append(x)

def is_prime(x):
    return all([x%j != 0 for j in range(2, int(x**0.5) + 1)])

for i in list_of_num:
    power_of_2 = 2 
    if is_prime(i):
        s = sum([int(n) for n in str(i)])
        print(f"Сумма цифр простого числа {i} = {s}")
    else: 
        while power_of_2 < i: 
            power_of_2 *= 2
        print(f"Ближайшая сверху к {i} степень двойки равна {power_of_2}")
        