# Імпортуємо модуль random для генерації випадкових чисел 
import random

# Створюємо функцію і задаємо їй відповідні параметри
def get_numbers_ticket():
    
    # Просимо користувача ввести мінімальне число для лотереї
    min_number = int(input("Введіть мінімальне число (>=1): "))
    # Просимо користувача ввести максимальне число для лотереї
    max_number = int(input("Введіть максимальне число (<=1000): "))
    # Просимо користувача ввести кількість чисел на квитку 
    quantity = int(input("Введіть кількість чисел для квитка: "))

    # Перевірка чи параметри правильні 
    if min_number < 1 or max_number > 1000 or min_number > max_number:
        print("Некоректні значення мінімуму i максимуму!")
        return
    elif quantity < 1 or quantity > (max_number - min_number + 1):
        print("Некоректна кількість чисел для квитка!")
        return

    # Генерація унікальних випадкових чисел
    ticket = random.sample(range(min_number, max_number + 1), quantity)

    # Сортуємо числа 
    ticket.sort()

    # Виводимо результат 
    print("Ваш лотерейний квиток:", ticket)
    print("Мінімальне число:", ticket[0])
    print("Максимальне число:", ticket[-1])
    print("Кількість чисел:", len(ticket))

get_numbers_ticket()



