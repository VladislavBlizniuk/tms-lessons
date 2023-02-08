# Напишите функцию generate_squares, которая принимает произвольное количество аргументов
# и возвращает список, состоящий из их квадратов.
# То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*xyz):
    list_squares = [ i ** 2 for i in xyz]
    return list_squares


print(generate_squares(1, 2, 3, 4))