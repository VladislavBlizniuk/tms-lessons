import random
n = random.randint(1, 10)
while True:
    a = int(input('Enter a namber: '))
    if a == n:
        print('Well done')
        break
        if a > n:
            print('не угадал, ваше число больше загаданного')
        if a < n:
            print('не угадал, ваше число меньше загаданного')
