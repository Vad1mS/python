import random

print("\n\nСформований список із 30 випадкових цілих чисел від -100 до +100:")

array = range(-100, 100)

numbers = random.sample(array, 30)

print(numbers)


print("\nМаксимальний елемент:")

print(max(numbers))

print("\nПорядковий номер максимального елементу списку:")

print(numbers.index(max(numbers)))


print("\nПари від’ємних чисел, що стоять поруч:\n")

for i in range(len(numbers)-1):

    if numbers[i] < 0 and numbers[i+1] < 0:

        print(numbers[i], numbers[i+1])