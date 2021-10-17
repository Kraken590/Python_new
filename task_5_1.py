# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
a = int(input('Введите число: '))


def my_gen():
    for i in range(a):
     if i % 2 != 0:
         yield i

s = my_gen()
print(next(s))




