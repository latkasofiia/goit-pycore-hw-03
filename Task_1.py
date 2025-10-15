# Імпортуємо модуль datetime, date
from datetime import datetime

# Функція приймає параметр(date), що представляє дату у форматі 'PPPP-MM-ДД'
def get_days_from_today(date_str):
 
    try:
        # Перетворюємо текстову дату у формат дати
        user_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        # Отримуємо сьогоднішню дату
        today = datetime.today().date()
        # Рахуємо різницю між поточною датою та заданою датою
        difference = today - user_date
        # Повертаємо кількість днів
        return difference.days
    
    except ValueError:
        # Якщо користувач ввів не правильну дату виводимо такий текст
        print("Помилка: введіть дату y форматі 'PPPP-MM-ДД'.")
        return None

# Просимо користувача ввести дату
user_input = input("Введіть дату y форматі 'PPPP-MM-ДД': ")
# Викликаємо функцію та виводимо результат
days = get_days_from_today(user_input)

if days is not None:
    print(f"Кількість днів від {user_input} до сьогодні: {days}")



