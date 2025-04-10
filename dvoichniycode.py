import timeit
import random

# Генерация и сортировка списка
arr = sorted(random.sample(range(1, 51), 10))  # Уникальные случайные числа от 1 до 50
print("Массив:", arr)

# Ввод искомого значения
target = int(input("Введите число для поиска: "))

# Бинарный поиск как отдельная функция
def binary_search(data, target):
    count = 0
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        count += 1
        if data[mid] == target:
            return f"Найден элемент на позиции {mid} (итераций: {count})"
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return f"Элемент не найден (итераций: {count})"

# Засекаем время выполнения
start_time = timeit.default_timer()
result = binary_search(arr, target)
elapsed = timeit.default_timer() - start_time

# Вывод результатов
print(result)
print(f"Время выполнения: {elapsed:.6f} секунд")