# Напишите функцию is_year_leap, которая принимает число (год)
# и возвращает True если год високосный
# (см. комментарий к слайда), False если нет.
a = int(input())
def is_year_leap(a) -> bool:
    return a % 4 == 0 and a % 100 != 0


print(is_year_leap(a))