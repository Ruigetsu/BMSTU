list_of_num = list(map(int, input("Введите числа через пробел: ").split()))
k = int(input("Введите номер экстремума: "))
extremums = []
for i in range(1,len(list_of_num)-1): #Проходимся по каждому элементу списка начиная с первого, заканчивая предпоследним
    if list_of_num[i] == max(list_of_num[i-1:i+2]) or list_of_num[i] == min(list_of_num[i-1:i+2]): #Если больше соседних ИЛИ меньше соседних
        extremums.append(list_of_num[i])

if len(extremums) > 0 and k > 0 and len(list_of_num) >= 3: #Если нашелся хоть одтн экстремум, номер экстремума положительный или длина списка не меньше 3
    print(f"Экстремум №{k} в списке {list_of_num} = {extremums[k-1]}")
else:
    print(f"Список слишком маленький,либо число k неположительное, либо экстремумов не найдено")

