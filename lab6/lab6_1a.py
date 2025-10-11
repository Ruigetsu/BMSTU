list_of_num = list(map(int,input("Введите элементы списка через пробел: ").split()))
num = int(input("Введите элемент для вставки: "))
indx = int(input("Введите индекс вставки элемента: "))
list_of_num.insert(indx,num)
if indx > len(list_of_num) or indx < -len(list_of_num) - 1:
    print("Вы ввели неверный индекс")
print(f"Новый список = {list_of_num}")
