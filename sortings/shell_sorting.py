import time
from sortings_func import generate_test_data

def shell_sort(arr):
    """
    7. Сортировка вставками: метод Шелла
    """
    n = len(arr)
    iterations = 0
    comparisons = 0
    swaps = 0
    
    # Начальный шаг (последовательность Кнута)
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
        iterations += 1
    
    # Последовательное уменьшение шага
    while gap > 0:
        iterations += 1
        
        # Сортировка вставками с заданным шагом
        for i in range(gap, n):
            iterations += 1
            temp = arr[i]
            j = i
            
            # Сдвигаем элементы, пока не найдем правильную позицию
            while j >= gap:
                iterations += 1
                comparisons += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break
            
            arr[j] = temp
            swaps += 1
        
        # Уменьшаем шаг
        gap //= 3
    
    return iterations, comparisons, swaps



def run_shell_sort_test():
    """
    Запуск теста сортировки Шелла
    """
    print("=== СОРТИРОВКА ШЕЛЛА ===")
    print(f"Размер списка: 1000 элементов")
    print()
    
    # Тестируем на разных типах данных
    test_cases = [
        ('Случайные данные', 'random'),
        ('Уже отсортированные данные', 'sorted'),
        ('Данные в обратном порядке', 'reversed')
    ]
    
    for test_name, data_type in test_cases:
        print(f"--- {test_name} ---")
        
        # Генерируем тестовые данные
        test_data = generate_test_data(1000, data_type)
        original_data = test_data.copy()
        
        # Замеряем время выполнения
        start_time = time.time()
        iterations, comparisons, swaps = shell_sort(test_data)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Проверяем корректность сортировки
        is_sorted = all(test_data[i] <= test_data[i + 1] for i in range(len(test_data) - 1))
        
        # Выводим результаты
        print(f"Время выполнения: {execution_time:.6f} секунд")
        print(f"Общее количество итераций: {iterations}")
        print(f"Количество сравнений: {comparisons}")
        print(f"Количество обменов: {swaps}")
        print(f"Корректно отсортирован: {'Да' if is_sorted else 'Нет'}")
        print()

def shell_sorting():
    run_shell_sort_test()

    # Дополнительный тест с разными размерами
    print("\n=== ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ===")
    sizes = [100, 500, 1000, 10000, 100000, 1000000]

    for size in sizes:
        test_data = generate_test_data(size, 'random')
        start_time = time.time()
        iterations, comparisons, swaps = shell_sort(test_data)
        end_time = time.time()
        
        print(f"Размер: {size:4d} | Время: {end_time - start_time:.6f} сек | "
              f"Итерации: {iterations:6d} | Сравнения: {comparisons:8d} | "
              f"Обмены: {swaps:6d}")
