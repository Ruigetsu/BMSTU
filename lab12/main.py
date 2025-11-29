from lab12_functions import print_array, input_with_check
from lab12_1 import lab12_1
from lab12_2 import lab12_2
from lab12_3 import lab12_3
from lab12_4 import lab12_4
from lab12_5 import lab12_5
from lab12_6 import lab12_6
from lab12_7 import lab12_7

menu_text = "\n1. Выровнять текст по левому краю \n\
2. Выровнять текст по правому краю \n\
3. Выровнять текст по ширине \n\
4. Удалить все вхождения введенного слова \n\
5. Заменить одно слово на другое во всем тексте \n\
6. Вычислить значения арифмитических выражений, содержащих умножение или деление, во всем тексте \n\
7. Найти и вывести, а затем удалить предложение с максимальным количеством слов, начинающихся на заданную букву.\n"

array = ["  В начале 180600/5/20/*-го года Николай Ростов вернулся",
         "в отпуск. Денисов ехал тоже домой",
         "в Воронеж. Ростов уговорил его ехать с собой до Москвы и остановиться     ",
         "у них в доме. На предпоследней станции, встретив товарища,  ",
         "   Денисов выпил с ним 6/2*2/2*1+1 бутылки вина. Подъезжая к Москве, несмотря на ухабы дороги,он не просыпался,    ",
         "лежа на дне",
         "перекладных",
         " саней, подле Ростова. Ростов по мере приближения к Москве       ",
         "      приходил все более и более в нетерпение."]
last_comand = None
while True:
    print(menu_text) 
    inp = input("Введите номер задания: ")
    print("")
    match inp: 
        case "1": 
            array = lab12_1(array)
            print_array(array)
            last_comand = 1
        case "2": 
            array = lab12_2(array)
            print_array(array)
            last_comand = 2
        case "3":
            array = lab12_3(array) 
            print_array(array)
            last_comand = 3
        case "4": 
            word = input_with_check("Введите слово: ")
            array,count = lab12_4(array,word)
            if last_comand == 1:
                array = lab12_1(array)
            elif last_comand == 2:
                array = lab12_2(array)
            elif last_comand == 3: 
                array = lab12_3(array)
            print_array(array)
            print(f"\nВ списке нашлось {count} слов, содержащих '{word}'.")
        case "5": 
            word_to_replace = input_with_check("Введите слово, которое надо заменить: ")
            word = input_with_check("Введите слово, которым надо заменить: ")
            array,count = lab12_5(array,word_to_replace,word)
            if last_comand == 1:
                array = lab12_1(array)
            elif last_comand == 2:
                array = lab12_2(array)
            elif last_comand == 3: 
                array = lab12_3(array)
            print_array(array)
            print(f"\nКоличество замен = {count}")
        case "6": 
            array = lab12_6(array)
            if last_comand == 1:
                array = lab12_1(array)
            elif last_comand == 2:
                array = lab12_2(array)
            elif last_comand == 3: 
                array = lab12_3(array)
            print_array(array)
        case "7":
            letter = input_with_check("Введите букву: ")
            sentence, array = lab12_7(array,letter)
            if last_comand == 1:
                array = lab12_1(array)
            elif last_comand == 2:
                array = lab12_2(array)
            elif last_comand == 3: 
                array = lab12_3(array) 
            print(sentence,"\n")
            print_array(array)
        case "0":
            print("Вы завершили программу!") 
            break
        case _:
            print("Вы ввели неправильный номер задания")