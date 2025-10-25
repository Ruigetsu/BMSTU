print("Введите номер задания или 0 для выхода:\n\
      Для задания 1 введите : 1\n\
      Для задания 2 введите : 2\n\
      Для задания 3 введите : 3\n\
      Для задания 4 введите : 4\n\
      Для задания 5 введите : 5\n\
      Для задания 6 введите : 6\n\
      Для завершения введите: 0\n")

while True: 
      exercise = input("Введите номер задания: ")
      match exercise:
            case "1":
                  exec(open("lab8_1_1.py", encoding='utf-8').read())
                  print("\n")
            case "2":
                  exec(open("lab8_2.py", encoding='utf-8').read())
                  print("\n")
            case "3":
                  exec(open("lab8_3_3.py", encoding='utf-8').read())
                  print("\n")
            case "4":
                  exec(open("lab8_4.py", encoding='utf-8').read())
                  print("\n")
            case "5":
                  exec(open("lab8_5.py", encoding='utf-8').read())
                  print("\n")
            case "6":
                  exec(open("lab8_6.py", encoding='utf-8').read())
                  print("\n")
            case "0":
                  print("Завершение работы")
                  break
            case _:
                  print("Вы ввели неправильное число")