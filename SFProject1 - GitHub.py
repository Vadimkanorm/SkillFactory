import numpy as np


number = np.random.randint(1, 101)


def game_core_v3(number):  # Вводим функцию - будем искать число, деля интервал поиска на 2
    count = 1  # Вводим счётчик. Тк ниже до цикла делаем первый guess, его значение 1
    leftborder = 1  # Вводим переменную - нижнюю границу значения угадываемого чила
    rightborder = 100  # Вводим переменную верхнюю границу значения угадываемого чила
    predict = (leftborder + rightborder) // 2  # Вводим переменную для загадываемого числа - середина интервала.
    while number != predict:  # Пока не будет найдено искомое число
        count += 1  # Рост счётчика
        if number > predict:
            leftborder = (leftborder + rightborder) // 2  # Если загаданное число меньше
        elif number < predict:
            rightborder = (leftborder + rightborder) // 2
        return count  # Выход из цикла, если угадали


game_core_v3(number)


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v3)
