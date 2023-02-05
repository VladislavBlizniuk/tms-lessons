import random
n = random.randint(1, 10)
while True:
    a = int(input('Enter a namber: '))
    if int(a) == n:
        print('Well done')
        break
    elif int(a) >= n:
        print('не угадал, ваше число больше загаданного')
        continue
    elif int(a) <= n:
        print('не угадал, ваше число меньше загаданного')
