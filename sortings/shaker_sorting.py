import random
import time

def shaker_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    iterations = 0
    comparisons = 0
    swaps = 0
    while left <= right:
        iterations += 1
        # Проход слева направо (как в обычной пузырьковой сортировке)
        for i in range(left, right):
            iterations += 1
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
        right -= 1  # Уменьшаем правую границу
        
        # Проход справа налево
        for i in range(right, left, -1):
            iterations += 1
            comparisons += 1
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swaps += 1
        left += 1  # Увеличиваем левую границу
    
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

def run_bubble_sort_test():
    """
    Запуск теста пузырьковой сортировки
    """
    print("=== ТЕСТ ПУЗЫРЬКОВОЙ СОРТИРОВКИ ===")
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
        original_data = test_data.copy()  # Сохраняем оригинал для проверки
        
        # Замеряем время выполнения
        start_time = time.time()
        iterations, comparisons, swaps = shaker_sort(test_data)
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

def shaker_sorting():
    run_bubble_sort_test()
    #detailed_analysis()

    # Дополнительный тест с разными размерами
    print("\n=== ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ===")
    sizes = [100, 500, 1000, 10000]

    for size in sizes:
        test_data = generate_test_data(size, 'random')
        start_time = time.time()
        iterations, comparisons, swaps = shaker_sort(test_data)
        end_time = time.time()
        
        print(f"Размер: {size:4d} | Время: {end_time - start_time:.6f} сек | "
                f"Итерации: {iterations:6d} | Сравнения: {comparisons:8d} | "
                f"Обмены: {swaps:6d}")