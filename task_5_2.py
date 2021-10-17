'''Решить задачу генерации нечётных чисел от 1 до n (включительно),
 не используя ключевое слово yield.'''

a = int(input('Введите число: '))

counter = (i for i in range(a) if i % 2 != 0)
for i in counter:
    print(i)