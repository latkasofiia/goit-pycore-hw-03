import re

def normalize_phone(phone_number: str) -> str:
    
    # Видаляємо всі символи, крім цифр і '+'
    phone = re.sub(r"[^\d+]", "", phone_number.strip())

    # Якщо номер вже починається з '+', повертаємо як є
    if phone.startswith('+'):
        return phone
    
    # Якщо номер починається з '380', додаємо '+'
    if phone.startswith('380'):
        return '+' + phone
    
    # Якщо номер починається з '0', додаємо '+38'
    if phone.startswith('0'):
        return '+38' + phone
    
    # Для всіх інших випадків додаємо '+38'
    return '+38' + phone


# Список номерів для перевірки
raw_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Нормалізуємо номери
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
