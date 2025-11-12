import random
import time
import sys

def quick_sort(arr):
    """
    10. Быстрая сортировка (рекурсивная версия с подсчетом вызовов)
    """
    iterations = [0]
    comparisons = [0]
    swaps = [0]
    recursive_calls = [0]
    
    def _quick_sort(arr, low, high):
        recursive_calls[0] += 1
        iterations[0] += 1
        
        if low < high:
            # Разделение массива и получение индекса опорного элемента
            pi = partition(arr, low, high)
            
            # Рекурсивная сортировка левой и правой частей
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)
    
    def partition(arr, low, high):
        # Выбираем опорный элемент (последний элемент)
        pivot = arr[high]
        
        # Индекс меньшего элемента (указывает на правильную позицию опорного элемента)
        i = low - 1
        
        for j in range(low, high):
            iterations[0] += 1
            comparisons[0] += 1
            
            # Если текущий элемент меньше или равен опорному
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0] += 1
        
        # Помещаем опорный элемент в правильную позицию
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps[0] += 1
        
        return i + 1
    
    # Увеличиваем глубину рекурсии для больших массивов
    sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr) + 1000))
    
    # Запускаем рекурсивную сортировку
    _quick_sort(arr, 0, len(arr) - 1)
    
    return iterations[0], comparisons[0], swaps[0], recursive_calls[0]

def generate_test_data(size=1000, data_type='random'):
    """
    Генерация тестовых данных
    """
    if data_type == 'random':
        return [random.randint(1, 100000) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(1, size + 1))
    elif data_type == 'reversed':
        return list(range(size, 0, -1))
    else:
        return [random.randint(1, 100000) for _ in range(size)]

def run_quick_sort_test():
    """
    Запуск теста быстрой сортировки
    """
    print("=== БЫСТРАЯ СОРТИРОВКА (РЕКУРСИВНАЯ) ===")
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
        iterations, comparisons, swaps, recursive_calls = quick_sort(test_data)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Проверяем корректность сортировки
        is_sorted = all(test_data[i] <= test_data[i + 1] for i in range(len(test_data) - 1))
        
        # Выводим результаты
        print(f"Время выполнения: {execution_time:.6f} секунд")
        print(f"Общее количество итераций: {iterations}")
        print(f"Количество сравнений: {comparisons}")
        print(f"Количество обменов: {swaps}")
        print(f"Количество рекурсивных вызовов: {recursive_calls}")
        print(f"Корректно отсортирован: {'Да' if is_sorted else 'Нет'}")
        print()

def quick_sorting():
    run_quick_sort_test()

    # Дополнительный тест с разными размерами
    print("\n=== ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ===")
    sizes = [100, 500, 1000, 10000, 100000, 1000000]

    for size in sizes:
        test_data = generate_test_data(size, 'random')
        start_time = time.time()
        iterations, comparisons, swaps, recursive_calls = quick_sort(test_data)
        end_time = time.time()
        
        print(f"Размер: {size:4d} | Время: {end_time - start_time:.6f} сек | "
              f"Итерации: {iterations:6d} | Сравнения: {comparisons:8d} | "
              f"Обмены: {swaps:6d} | Рекурсивные вызовы: {recursive_calls:6d}")