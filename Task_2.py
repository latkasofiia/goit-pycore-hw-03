# Імпортуємо модуль random для генерації випадкових чисел
import random

# Створюємо функцію і задаємо їй відповідні параметри
def get_numbers_ticket(min_num, max_num, quantity):
    
    # Перевірка коректності параметрів
    if min_num < 1 or max_num > 1000 or min_num > max_num:
        return []
    if quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    # Генерація унікальних випадкових чисел
    ticket = random.sample(range(min_num, max_num + 1), quantity)

    # Сортуємо числа
    ticket.sort()


# Виводимо результат
    print("Ваш лотерейний квиток:", ticket)
    print("Мінімальне число:", ticket[0])
    print("Максимальне число:", ticket[-1])
    print("Кількість чисел:", len(ticket))

    return ticket

# Просимо користувача ввести параметри
min_number = int(input("Введіть мінімальне число (>=1): "))
max_number = int(input("Введіть максимальне число (<=1000): "))
quantity = int(input("Введіть кількість чисел для квитка: "))

get_numbers_ticket(min_number, max_number, quantity)
