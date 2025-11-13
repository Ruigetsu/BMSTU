import random

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