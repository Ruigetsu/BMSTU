import time
from sortings_func import generate_test_data

def bidirectional_selection_sort(arr):
    """
    9. Двунаправленная сортировка выбором
    """
    n = len(arr)
    iterations = 0
    comparisons = 0
    swaps = 0
    
    left = 0
    right = n - 1
    
    while left < right:
        iterations += 1
        
        min_index = left
        max_index = right
        
        # Находим индексы минимального и максимального элемента в неотсортированной части
        for i in range(left, right + 1):
            iterations += 1
            comparisons += 1
            if arr[i] < arr[min_index]:
                min_index = i
            
            comparisons += 1
            if arr[i] > arr[max_index]:
                max_index = i
        
        # Меняем минимальный элемент с первым неотсортированным
        if min_index != left:
            arr[left], arr[min_index] = arr[min_index], arr[left]
            swaps += 1
        
        # Если максимальный элемент был на позиции left, он переместился на min_index
        if max_index == left:
            max_index = min_index
        
        # Меняем максимальный элемент с последним неотсортированным
        if max_index != right:
            arr[right], arr[max_index] = arr[max_index], arr[right]
            swaps += 1
        
        # Сужаем диапазон
        left += 1
        right -= 1
    
    return iterations, comparisons, swaps


def run_bidirectional_selection_sort_test():
    """
    Запуск теста двунаправленной сортировки выбором
    """
    print("=== ДВУНАПРАВЛЕННАЯ СОРТИРОВКА ВЫБОРОМ ===")
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
        iterations, comparisons, swaps = bidirectional_selection_sort(test_data)
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

def bidirectional_selection_sorting():
    run_bidirectional_selection_sort_test()

    # Дополнительный тест с разными размерами
    print("\n=== ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ===")
    sizes = [100, 500, 1000, 10000]

    for size in sizes:
        test_data = generate_test_data(size, 'random')
        start_time = time.time()
        iterations, comparisons, swaps = bidirectional_selection_sort(test_data)
        end_time = time.time()
        
        print(f"Размер: {size:4d} | Время: {end_time - start_time:.6f} сек | "
              f"Итерации: {iterations:6d} | Сравнения: {comparisons:8d} | "
              f"Обмены: {swaps:6d}")
