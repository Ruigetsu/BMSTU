import time
from sortings_func import generate_test_data
def insertion_sort_with_sentinel(arr):
    n = len(arr)
    
    iterations = 0

    swaps = 0
    
    sentinel = min(arr) - 1  # Значение гарантированно меньше всех элементов
    arr.insert(0, sentinel)
    
    # Сортируем массив с барьером
    for i in range(2, n + 1):
        iterations += 1
        key = arr[i]
        j = i - 1
        
        # Убираем проверку j >= 0 благодаря барьеру
        while True:
            iterations += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        
        arr[j + 1] = key
        swaps += 1
    
    arr.pop(0)
    
    return iterations,swaps

def run_sentinel_sort_test():
    """
    Запуск теста сортировки вставками с барьером
    """
    print("=== СОРТИРОВКА ВСТАВКАМИ С БАРЬЕРОМ ===")
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
        iterations, comparisons, swaps = insertion_sort_with_sentinel(test_data)
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

def sentinel_insertion_sorting():
    run_sentinel_sort_test()

    # Дополнительный тест с разными размерами
    print("\n=== ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ===")
    sizes = [100, 500, 1000, 10000]

    for size in sizes:
        test_data = generate_test_data(size, 'random')
        start_time = time.time()
        iterations, comparisons, swaps = insertion_sort_with_sentinel(test_data)
        end_time = time.time()
        
        print(f"Размер: {size:4d} | Время: {end_time - start_time:.6f} сек | "
              f"Итерации: {iterations:6d} | Сравнения: {comparisons:8d} | "
              f"Обмены: {swaps:6d}")