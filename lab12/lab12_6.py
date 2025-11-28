from lab12_functions import check_int

def lab12_6(array):
    result_array = []
    
    for i in range(len(array)):
        result = ""
        j = 0
        string = array[i]
        
        while j < len(string):
            if string[j].isdigit(): 
                expression = ""
                while j < len(string):
                    if string[j].isdigit():
                        number = ""
                        while j < len(string) and string[j].isdigit():  # собираем одно число
                            number += string[j]
                            j += 1
                        expression += number

                        if j < len(string) and string[j] in ['*', '/']:
                            expression += string[j]
                            j += 1
                        else:
                            break
                    elif string[j-1] in ['*', '/']: #если два знака подряд
                        expression = expression[:-1]
                        j -= 1
                        break
                    else: 
                        break
                print(expression)
                if '*' in expression or '/' in expression:  # одно число или выражение
                    nums_and_ops = []
                    current_number = ""
                    
                    for char in expression:
                        if char.isdigit():
                            current_number += char
                        elif char in ['*', '/']:
                            if current_number:
                                num = check_int(current_number)
                                if num is not None:
                                    nums_and_ops.append(num)
                                    current_number = ""
                            nums_and_ops.append(char)

                    if current_number:
                        num = check_int(current_number)
                        if num is not None:
                            nums_and_ops.append(num)

                    value = nums_and_ops[0]
                    k = 1
                    division_by_zero = False                    
                    while k < len(nums_and_ops) - 1:
                        operator = nums_and_ops[k]
                        number = nums_and_ops[k + 1]
                        if operator == '*':
                            value *= number
                        elif operator == '/' and number != 0:
                            value /= number
                        else: 
                            division_by_zero = True
                            break
                        k += 2
                    
                    if division_by_zero: #если было деление на ноль - сохраняем выражение
                        result += expression
                    else:
                        if value == int(value):
                            result += str(int(value))
                        else:
                            result += str(value)
                else: #если число 1
                    result += expression
            else:
                result += string[j]
                j += 1
        
        result_array.append(result)
    
    return result_array
    
