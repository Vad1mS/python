##### _Генерація рандомного списку_
_import random_
_print("\n\nСформований список із 30 випадкових цілих чисел від -100 до +100:")_
_array = range(-100, 100)_
_numbers = random.sample(array, 30)_
****
#### _Пошук максимального значення в списку_
_print("\nМаксимальний елемент:")_
_print(max(numbers))_
_print("\nПорядковий номер максимального елементу списку:")_
_print(numbers.index(max(numbers)))_
****
#### _Пошук від'ємних чисел_
_print("\nПари від’ємних чисел, що стоять поруч:\n")_
_for i in range(len(numbers)-1):_
_if numbers[i] < 0 and numbers[i+1] < 0:_
****
#### _Результат_
_print(numbers[i], numbers[i+1])_

