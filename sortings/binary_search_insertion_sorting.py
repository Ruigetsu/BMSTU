import time
from sortings_func import generate_test_data

def binary_search_insertion_sort(arr):
    """
    6. Сортировка вставками: метод вставок с бинарным поиском
    """
    n = len(arr)
    iterations = 0
    comparisons = 0
    swaps = 0
    
    for i in range(1, n):
        iterations += 1
        key = arr[i]
        
        # Бинарный поиск позиции для вставки
        left = 0
        right = i - 1
        pos = i  # Позиция по умолчанию
        
        while left <= right:
            iterations += 1
            comparisons += 1
            mid = (left + right) // 2
            
            if arr[mid] == key:
                pos = mid + 1
                break
            elif arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        
        # Если позиция не найдена в цикле, определяем её
        if left > right:
            comparisons += 1
            pos = left
        
        # Сдвигаем элементы и вставляем key на найденную позицию
        for j in range(i, pos, -1):
            iterations += 1
            arr[j] = arr[j - 1]
            swaps += 1
        
        arr[pos] = key
        swaps += 1  # Вставка элемента
    
    return iterations, comparisons, swaps

def run_binary_insertion_sort_test():
    """
    Запуск теста сортировки вставками с бинарным поиском
    """
    print("=== СОРТИРОВКА ВСТАВКАМИ С БИНАРНЫМ ПОИСКОМ ===")
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
        iterations, comparisons, swaps = binary_search_insertion_sort(test_data)
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

def binary_insertion_sorting():
    run_binary_insertion_sort_test()

    # Дополнительный тест с разными размерами
    print("\n=== ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ===")
    sizes = [100, 500, 1000, 10000]

    for size in sizes:
        test_data = generate_test_data(size, 'random')
        start_time = time.time()
        iterations, comparisons, swaps = binary_search_insertion_sort(test_data)
        end_time = time.time()
        
        print(f"Размер: {size:4d} | Время: {end_time - start_time:.6f} сек | "
              f"Итерации: {iterations:6d} | Сравнения: {comparisons:8d} | "
              f"Обмены: {swaps:6d}")

