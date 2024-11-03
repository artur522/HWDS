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


def binary_predict(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low, high = 1, 100  # начальные границы поиска
    
    while low <= high:
        count += 1
        predict_number = (low + high) // 2  # середина диапазона
        
        if predict_number == number:
            break  # выход из цикла если угадали
        elif predict_number < number:
            low = predict_number + 1  # сдвигаем нижнюю границу
        else:
            high = predict_number - 1  # сдвигаем верхнюю границу
            
    return count


def score_game(predict_function) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_function ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # Запуск с функцией random_predict
    print("Результат для random_predict:")
    score_game(random_predict)
    
    # Запуск с функцией binary_predict
    print("\nРезультат для binary_predict:")
    score_game(binary_predict)
