# Створюємо функцію 
def normalize_phone(phone_number):
    
    # Видаляємо пробіли, дужки, тире
    cleaned = phone_number.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
    
    # Додаємо код країни, якщо його немає
    if cleaned.startswith("0"):
        cleaned = "+38" + cleaned
    elif cleaned.startswith("380"):
        cleaned = "+" + cleaned
    elif cleaned.startswith("+38"):
        pass
    else:
        cleaned = "+38" + cleaned
    
    return cleaned

# Список номерів
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
