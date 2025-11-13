import time
from sortings_func import generate_test_data
def bubble_sort_with_flag(data):
    n = len(data)
    iterations = 0
    comparisons = 0
    swaps = 0
    for i in range(n):
        iterations += 1
        swapped = False
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            iterations += 1
            comparisons += 1
            if data[j] > data[j + 1]:
                # Меняем местами, если предыдущий больше последующего
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                swaps += 1
        # Если обменов не было, значит список отсортирован
        if not swapped:
            break
    return iterations, comparisons, swaps

def run_test():
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
        iterations, comparisons, swaps = bubble_sort_with_flag(test_data)
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

def bubble_sorting_with_flag():
    run_test()
    #detailed_analysis()

    # Дополнительный тест с разными размерами
    print("\n=== ТЕСТ С РАЗНЫМИ РАЗМЕРАМИ ===")
    sizes = [100, 500, 1000, 10000]

    for size in sizes:
        test_data = generate_test_data(size, 'random')
        start_time = time.time()
        iterations, comparisons, swaps = bubble_sort_with_flag(test_data)
        end_time = time.time()
        
        print(f"Размер: {size:4d} | Время: {end_time - start_time:.6f} сек | "
                f"Итерации: {iterations:6d} | Сравнения: {comparisons:8d} | "
                f"Обмены: {swaps:6d}")
