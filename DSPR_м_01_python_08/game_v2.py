"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


#if __name__ == "__main__":
    # RUN
    score_game(random_predict)


def game_core_v3(number: int = 1) -> int:
    """Применяем метод деления пополам. Делим сумму максимального и минимального значения пополам.
    Полученный результат сравниваем с загаданным числом, и в зависимости от того, больше оно или меньше
    заменяем  минимальное и максимальное значение.
    Считаем среднее кол-во попыток.

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count = 0
    number_max = 102
    number_min = 0
        
    while True:
        predict = round((number_max + number_min)/2)
        count +=1
        if number > predict:
            number_min = predict
        elif number < predict:
            number_max = predict
        elif number == predict:
            break
            
    return count


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
    
    
    