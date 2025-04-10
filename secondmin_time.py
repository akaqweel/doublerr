import timeit
import time

# Засекаем время начала
start = timeit.default_timer()
print("Start time:", start)

# Эмуляция задержки
time.sleep(20)

# Пример массива
arr = [1, 1, 1, 1, 2]

# Инициализируем минимумы
first_min = float('inf')
second_min = float('inf')

# Находим минимальные значения
for num in arr:
    if num < first_min:
        second_min = first_min
        first_min = num
    elif first_min < num < second_min:
        second_min = num

# Проверка наличия второго минимума
if second_min == float('inf'):
    print("Второго минимального элемента нет.")
else:
    print("Второй минимум:", second_min)

# Показываем разницу во времени
print("Execution time:", timeit.default_timer() - start)