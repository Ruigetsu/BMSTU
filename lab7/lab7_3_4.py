list_of_str = []
while True:
    string = input("Введите строку: ")
    if string == "":
        break
    else:
        list_of_str.append(string)

max_spaces = -1
indx_of_max_spaces = 0
for i in range(len(list_of_str)):
    curr_str = list_of_str[i]
    curr_spaces = 0
    if curr_str.count(" ") > max_spaces: #Если общее кол-во пробелов в строке больше максимума
        for char in curr_str: #Проходимся по каждому элементу
            if char == " ": 
                curr_spaces += 1
            else: 
                if curr_spaces > max_spaces: 
                    max_spaces = curr_spaces
                    indx_of_max_spaces = i
                    curr_spaces = 0
        if curr_spaces > max_spaces: #Если строчка заканчивается пробелами
            max_spaces = curr_spaces
            indx_of_max_spaces = i
    else: 
        continue
print(f"Элемент с максимальным числом идущий подряд пробелов: '{list_of_str[indx_of_max_spaces]}'")