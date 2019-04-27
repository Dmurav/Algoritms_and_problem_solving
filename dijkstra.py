
# Создаём граф на основе стандартного словаря,
# поскольку он позволяет устанавливать отношения
# между объектами. Каждому ключу, который в данном случае
# является вершиной графа присвоен вес - расстояние между
# вершинами.
graph = dict()
# Устанавливаем стартовую точку
graph["start"] = dict()
# Обозначаем рассточние от старта до точек
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# Устанавливаем точку а и её соседей
graph["a"] = dict()
# Обозначаем рассточние от а до финиша
graph["a"]["fin"] = 1
# Устанавливаем точку в и её соседей
graph["b"] = dict()
# Обозначаем рассточние от в до а
graph["b"]["a"] = 3
# Обозначаем рассточние от в до финиша
graph["b"]["fin"] = 5
# У конечного узла "финиш" нет соседей
graph["fin"] = dict()

infinity = float("inf")

# Инициируем словарь - стоимости узлов
costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Инициируем словарь - родители
parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs)-> str:
    """Вспомогательная функция.
    Функция получает на вход словарь - затраты
    возвращает точку до которой от начальной точки
    наименьшее расстояние"""
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def get_nearest_path() -> int:
    """Функция не принимает аргументов, но инициализирует
    вспомогательную функцию, получая её производные.
    Алгоритм находит все необработанные вершины(узлы).
    Функция возвращает итоговую стоимость кратчайшего пути."""
    node = find_lowest_cost_node(costs)  # Полуаем узел для обработки
    while node is not None:  # Пока есть узлы цикл продолжается
        cost = costs[node]  # Получаем стоимость текущего узла
        neighbors = graph[node]  # Получаем соседей текущего узла
        for n in neighbors.keys(): # Для каждого соседа в соседях
            new_cost = cost + neighbors[n]  # вычисляем итоговую стоимость передвижения
            if costs[n] > new_cost:  # если старая стоимость больше новой
                costs[n] = new_cost  # выбираем новый путь
                parents[n] = node
        processed.append(node)  # Добавляем узел в обработанные
        node = find_lowest_cost_node(costs)  # Добавляем новый узел для обработки
    return cost


def test_dijkstra():
    result = get_nearest_path()
    assert result == 6


print("Самое короткое расстояние \n"
      "от старта до финиша - "
      + str(get_nearest_path()) + " условных единиц пути")
