import timeit
import random

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"Найден {target} на позиции {mid}, шагов: {steps}"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return f"{target} не найден, шагов: {steps}"

# Повторяем эксперимент 10 раз
for run in range(10):
    print(f"\n Прогон {run + 1}")
    numbers = sorted(random.choices(range(1, 50001), k=10000))
    print(f"Пример массива: {numbers[:10]} ... {numbers[-10:]}")  # Показываем только часть для краткости
    target = random.randint(1, 50)

    print(f"Ищем число: {target}")
    start = timeit.default_timer()
    result = binary_search(numbers, target)
    elapsed = timeit.default_timer() - start

    print(result)
    print(f"⏱ Время поиска: {elapsed:.6f} сек")