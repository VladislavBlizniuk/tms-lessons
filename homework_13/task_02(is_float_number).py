#Напишите функцию is_float_number, которая принимает строку и возвращает bool
#Функция должна вернуть True если переданная строка это корректное число с плавающей точкой.
import re


def is_float_number(string: str) -> bool:
    return re.fullmatch(r'[-+]?\d+\.\d+', string) is not None


if __name__ == '_main__':
    assert is_float_number('1.0')
    assert is_float_number('-1.0')
    assert not is_float_number('341.89')
    assert not is_float_number('25')
    assert not is_float_number('00000')
