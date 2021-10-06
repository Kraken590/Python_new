prices = [29.9, 40.05, 86, 01.5, 14.44, 56.98, 69.53, 125, 4555.34, 2004, 40.5]
# Вывел цены через запятую в одну строку, цена отображаться в виде <r> руб <kk> коп
for price in prices:
    rub = int(price)
    kk = (price - int(price)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=(','))

# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
print(f"\n\n{'#' * 60} 2\n")
print(f"ID base: {id(prices)} - {prices}")
prices.sort()
print(f"ID change: {id(prices)} - {prices}")

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров
print(f"\n\n{'#' * 60} 2\n")
n_list = sorted(prices, reverse=True)
print(f"ID change: {id(n_list)} - {n_list}\n{n_list[:5][::-1]}")