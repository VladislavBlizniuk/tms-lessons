#Напишите функцию is_date, которая принимает строку и возвращает bool.
#Функция должна вернуть True если переданная строка это дата в формате "DD-MM-YYYY"
import re

def is_date(string: str) -> bool:
    return re.fullmatch(r'\d\d-\d\d-\d{4}', string) is not None


if __name__ == '__main__':
    assert is_date('01-12-2022')
    assert not is_date('ff-12.2020')
    assert not is_date('01122022')
    assert not is_date('01.12.2022')