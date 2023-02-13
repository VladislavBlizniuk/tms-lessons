# Пользователь вводит произвольное количество маленьких латинских
# букв через пробел. Напишите функцию remove_vowels, которая принимает
# список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.

user = list(map(str, input().lower().split()))
vowels = ['a', 'e', 'i', 'o', 'u']

def remove_vowels(user):
    my_list = list(filter(lambda i: i not in vowels, user))
    return my_list

print(remove_vowels(user))