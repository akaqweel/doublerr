import timeit  # Модуль для измерения времени выполнения кода
import time    # Модуль для работы с паузами (задержками)

# Функция для подсчёта количества вершин в графе
def count_vertices(edges):
    """Подсчитывает количество уникальных вершин в графе (по рёбрам)."""
    vertices = set()  # Множество для хранения уникальных вершин
    for edge in edges:  # Перебираем все рёбра
        vertices.add(edge[0])  # Добавляем первую вершину
        vertices.add(edge[1])  # Добавляем вторую вершину
    return len(vertices)  # Возвращаем количество уникальных вершин

# Функция для получения списка вершин из рёбер
def get_vertices(edges):
    """Возвращает список всех уникальных вершин в графе."""
    vertices = set()  # Множество для хранения уникальных вершин
    for edge in edges:  # Перебираем все рёбра
        vertices.add(edge[0])  # Добавляем первую вершину
        vertices.add(edge[1])  # Добавляем вторую вершину
    return list(vertices)  # Преобразуем множество в список и возвращаем

# Функция для выполнения волнового алгоритма (поиск кратчайшего пути)
def wave_algorithm(edges, start, end):
    """Реализует волновой алгоритм для поиска кратчайшего пути."""
    
    # Получаем список вершин из рёбер
    vertices = get_vertices(edges)
    
    # Словарь для хранения информации о том, на каком шаге была посещена вершина
    visited = {v: 0 for v in vertices}
    visited[start] = 1  # Начинаем с начальной вершины, ей присваиваем шаг 1
    
    # Словарь для хранения родителей вершин (для восстановления пути)
    parent = {v: None for v in vertices}
    
    step = 1  # Шаг алгоритма
    found = False  # Флаг для проверки, найден ли путь
    
    while True:
        new_vertices_found = False  # Флаг, который говорит, что на текущем шаге были найдены новые вершины
        
        # Проходим по всем вершинам, которые были посещены на текущем шаге
        for v in vertices:
            if visited[v] == step:
                # Проходим по всем соседям вершины v
                for edge in edges:
                    if edge[0] == v and visited[edge[1]] == 0:  # Если соседа ещё не посещали
                        visited[edge[1]] = step + 1  # Отмечаем его как посещённый
                        parent[edge[1]] = v  # Записываем его родителя
                        new_vertices_found = True  # Новая вершина найдена
                    if edge[1] == v and visited[edge[0]] == 0:  # Проверяем и второй случай (неориентированные рёбра)
                        visited[edge[0]] = step + 1
                        parent[edge[0]] = v
                        new_vertices_found = True
        
        # Если конечная вершина найдена, выходим из цикла
        if visited[end] != 0:
            found = True
            break
        
        # Если на текущем шаге не было найдено новых вершин, завершаем алгоритм
        if not new_vertices_found:
            break
        
        step += 1  # Переходим к следующему шагу
    
    # Восстанавливаем путь, если конечная вершина была найдена
    if found:
        path = []  # Список для хранения пути
        current = end  # Начинаем с конечной вершины
        while current is not None:  # Восстанавливаем путь
            path.append(current)
            current = parent[current]
        path.reverse()  # Разворачиваем путь, чтобы он шёл от старта к концу
        return path, visited
    else:
        return None, visited  # Если пути нет, возвращаем None

# Пример использования

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), (7, 5)]  # Рёбра графа
start = 7  # Начальная вершина
end = 2    # Конечная вершина

# Замер времени для выполнения волнового алгоритма
start_time = timeit.default_timer()  # Начало измерения времени
print("Время начала выполнения волнового алгоритма:", start_time)

# Выполнение волнового алгоритма
path, visited = wave_algorithm(edges, start, end)

# Замер времени после выполнения
end_time = timeit.default_timer()  # Время после выполнения
print(f"Время выполнения волнового алгоритма: {end_time - start_time:.4f} сек")

# Печать результатов
if path:
    print(f"Кратчайший путь от {start} до {end}: {path}")
else:
    print(f"Путь от {start} до {end} не найден")

# Печать шагов посещения
print("Шаги посещения вершин:", visited)

# Подсчёт количества вершин в графе
start_time = timeit.default_timer()  # Начало замера времени
count = count_vertices(edges)
end_time = timeit.default_timer()  # Конец замера времени
print(f"Количество вершин в графе: {count}")
print(f"Время подсчёта количества вершин: {end_time - start_time:.4f} сек")

# Получение списка вершин
start_time = timeit.default_timer()  # Начало замера времени
vertices = get_vertices(edges)
end_time = timeit.default_timer()  # Конец замера времени
print(f"Список всех вершин: {vertices}")
print(f"Время получения вершин: {end_time - start_time:.4f} сек")