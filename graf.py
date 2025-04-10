from collections import deque

def build_graph(edges):
    """Создает словарь смежности из списка рёбер."""
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)  # для неориентированного графа
    return graph

def bfs_shortest_path(graph, start, end):
    """Реализация волнового (BFS) алгоритма."""
    visited = {start}
    parent = {start: None}
    queue = deque([start])
    steps = {start: 1}
    
    while queue:
        current = queue.popleft()
        if current == end:
            break
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                steps[neighbor] = steps[current] + 1
                queue.append(neighbor)
    
    # Восстановление пути
    if end not in parent:
        return None, steps
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    path.reverse()
    return path, steps

# Пример использования
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 6), (6, 7), (7, 5)]
start, end = 1, 5

graph = build_graph(edges)
path, steps = bfs_shortest_path(graph, start, end)

if path:
    print(f"Кратчайший путь от {start} до {end}: {path}")
else:
    print(f"Путь от {start} до {end} не найден")

print("Шаги посещения вершин:", steps)