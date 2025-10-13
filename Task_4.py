from datetime import datetime, timedelta

# Створюємо список 
users = [
    {"name": "John Doe", "birthday": "2025.10.15"},
    {"name": "Jane Smith", "birthday": "2025.10.18"},
    {"name": "Alice Brown", "birthday": "2025.10.19"}
]

def get_upcoming_birthdays(users):

    # Визначаємо поточну дату
    today = datetime.today().date()
    upcoming = []
    
    # Проходимся по списку та аналізуємо кожного користувача
    for user in users:

        # Конвертуємо дату народження із рядка в обʼєкт datatime 
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Перевіряємо, якщо день народження вже пройшов, беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until = (birthday_this_year - today).days

        if 0 <= days_until <= 7:
            # Перевірте, чи день народження припадає на вихідний, якщо так то переносим дату 
            if birthday_this_year.weekday() == 5: 
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  
                birthday_this_year += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming

# Виводимо зібрані дані
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)


