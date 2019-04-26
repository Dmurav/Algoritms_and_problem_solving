from collections import deque


# Создаём граф на основе стандартного словаря,
# поскольку он позволяет устанавливать отношения
# между объектами
graph = dict()
# Устанавливает отношение между своим именем и друзьями
graph["you"] = ["alice", "bob", "claire"]
# Вносим друзей Alice
graph["alice"] = ["peggy"]
# Вносим друзей Claire
graph["claire"] = ["thom", "jonny"]
# Вносим друзей Bob
graph["bob"] = ["anuj", "peggy"]
# Поскольку у друзей друзей нет друзей - обозначаем их пустыми списками
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    """Вспомогательная функция для проверки
    имени на критерий. Получает на вход имя,
    возвращает - True или False"""
    return name[-1] == 'm'


def search(name):
    """Алгоритм поиска в графе в ширину (breadth-first search),
    получает на вход имя искомого человека из друзей и знакомых,
    создаёт очередь для проверки имён, добавляет в очередь имена
    друзей друзей для проверки. Пока очередь не пуста, алгоритм
    достаёт из очереди имя и если имя не в списке проверенных,
    проверяет его. Если имя соответствует критерию - алгоритм печатает
    имя продавца манго и возвращает True. Иначе добавляет в очередь
    имена друзей проверенного имени."""
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                result = str(person) + " is a mango seller!"
                return result
            else:
                search_queue += graph[person]
    return False


def test_search():
    """Тест проверяет соответствие полученного результата
    заранее определённому эталону"""
    #Запускаем алгоритм поиска по графу вызывая функцию
    result = search("you")
    assert result == "thom is a mango seller!"

