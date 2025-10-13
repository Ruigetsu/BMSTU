x = y = 1
x_prev = y_prev = 1
for i in range(1,10+1): 
    print(f"элемент {i}: x = {x} y = {y}")
    x = 2*y_prev + x_prev
    y = 2*x_prev**2 + y_prev
    x_prev = x
    y_prev = y