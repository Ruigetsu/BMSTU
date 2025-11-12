import random
import time

def selection_sort(arr):
    """
    8. Простая сортировка выбором
    """
    n = len(arr)
    iterations = 0
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        iterations += 1
        
        # Находим индекс минимального элемента в неотсортированной части
        min_index = i
        for j in range(i + 1, n):
            iterations += 1
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Меняем местами найденный минимальный элемент с первым неотсортированным
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    
    return iterations, comparisons, swaps

def generate_test_data(size=1000, data_type='random'):
    """
    Генерация тестовых данных
    """
    if data_type == 'random':
        return [random.randint(1, 10000) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(1, size + 1))
    elif data_type == 'reversed':
        return list(range(size, 0, -1))
    else:
        return [random.randint(1, 10000) for _ in range(size)]

def run_selection_sort_test():
    """
    Запуск теста простой сортировки выбором
    """
    print("=== ПРОСТАЯ СОРТИРОВКА ВЫБОРОМ ===")
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
        iterations, comparisons, swaps = selection_sort(test_data)
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

def selection_sorting():
    run_selection_sort_test()

    # Дополнительный тест с разными размерами
    print("\n=== ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ===")
    sizes = [100, 500, 1000, 10000]

    for size in sizes:
        test_data = generate_test_data(size, 'random')
        start_time = time.time()
        iterations, comparisons, swaps = selection_sort(test_data)
        end_time = time.time()
        
        print(f"Размер: {size:4d} | Время: {end_time - start_time:.6f} сек | "
              f"Итерации: {iterations:6d} | Сравнения: {comparisons:8d} | "
              f"Обмены: {swaps:6d}")
