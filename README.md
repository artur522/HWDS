# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](#Описание-проекта)  
[2. Какой кейс решаем?](#Какой-кейс-решаем)  
[3. Краткая информация о данных](#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](#Этапы-работы-над-проектом)  
[5. Результаты](#Результаты)    
[6. Выводы](#Выводы) 

### Описание проекта    
Разработать алгоритм, который сможет угадать загаданное компьютером число за минимальное количество попыток.

:arrow_up:[к оглавлению](#Оглавление)

### Какой кейс решаем?    
Задача — написать программу, которая угадывает случайное число, загаданное компьютером, используя минимальное количество попыток.

**Условия:**  
- Компьютер загадывает целое число от 0 до 100, и программа должна угадать его.
- Алгоритм должен учитывать, больше или меньше предполагаемое число по сравнению с загаданным.

**Метрика качества:**     
Оценка производится по среднему количеству попыток для угадывания числа при 1000 повторениях.

**Навыки, которые можно развить:**     
- Оптимизация алгоритмов поиска.
- Написание эффективного и читаемого кода на Python.

:arrow_up:[к оглавлению](#Оглавление)

### Краткая информация о данных
Для тестирования алгоритма компьютер загадывает случайные числа от 1 до 100, а программа должна угадать каждое из этих чисел, фиксируя количество попыток для каждого случая. После 1000 повторений выводится среднее количество попыток.

:arrow_up:[к оглавлению](#Оглавление)

### Этапы работы над проектом  
1. Разработка простой версии алгоритма угадывания числа, который случайным образом генерирует предполагаемое число (функция `random_predict`).
2. Оптимизация алгоритма с использованием бинарного поиска для уменьшения количества попыток (функция `binary_predict`).
3. Написание функции `score_game` для автоматической оценки среднего количества попыток при угадывании числа.
4. Сравнение результатов двух подходов (рандомного и бинарного угадывания) для анализа производительности.

:arrow_up:[к оглавлению](#Оглавление)

### Результаты:  
- Реализован и протестирован алгоритм бинарного поиска, который угадывает число в среднем за меньшее количество попыток по сравнению с рандомным способом.
- Бинарный поиск позволяет угадать число в среднем менее чем за 20 попыток, что удовлетворяет целям задачи.

:arrow_up:[к оглавлению](#Оглавление)

### Выводы:  
Применение бинарного поиска существенно повысило эффективность программы. Данный проект демонстрирует, как правильный выбор алгоритма позволяет добиться значительного улучшения производительности. Использование бинарного поиска делает алгоритм быстродействующим и предсказуемым.

:arrow_up:[к оглавлению](#Оглавление)

Если информация по этому проекту покажется вам интересной или полезной, пожалуйста, оцените репозиторий и профиль ⭐️.
