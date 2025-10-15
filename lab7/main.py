print("Введите номер задания или 0 для выхода:\n\
      Для задания 1 введите : 1\n\
      Для задания 2 введите : 2\n\
      Для задания 3 введите : 3\n\
      Для задания 4 введите : 4\n\
      Для завершения введите: 0\n")

while True: 
      exercise = input("Введите номер задания: ")
      match exercise:
            case "1":
                  f = open("lab7_1_2.py").read()
                  exec(f)
                  print("\n")
            case "2":
                  f = open("lab7_2_2.py").read()
                  exec(f)
                  print("\n")
            case "3":
                  f = open("lab7_3_4.py").read()
                  exec(f)
                  print("\n")
            case "4":
                  f = open("lab7_4_3.py").read()
                  exec(f)
                  print("\n")
            case "0":
                  print("Завершение работы")
                  break
            case _:
                  print("Вы ввели неправильное число")