#Напишите функцию-генератор generate_words, которая принимает текст
#разбивает их на слова и отдаёт (yield) по одному.
def generate_words(string: str):
    list_str = string.split()
    for i in list_str:
        yield i


if __name__ == '__main__':
    string = 'мама мыла раму'
    for i in generate_words(string):
        print(i)

    assert ['мама', 'мыла', 'раму'] == [i for i in generate_words('мама мыла раму')]