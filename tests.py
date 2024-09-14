from decimal import Decimal
from datetime import date

from main import add, add_by_note, amount, expire, find


goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': date(2023, 9, 30)}
    ]
}

print("add and add_by_note check")
add(goods, 'Вода', Decimal('2.5'))
add_by_note(goods, "Яйца Гусиные 4.2 2023-07-15 ")
add_by_note(goods, "Яйца Гусиные 5 2025-07-17 ")
add_by_note(goods, "Яйца Гусиные 2 2025-10-17 ")
add_by_note(goods, 'Молоко 2.5')
print(goods)
print("--------------")
print("find check")
print(find(goods, "ца"))
print("--------------")
print("amount check")
print(amount(goods, "ца"))
print("--------------")
print("expire check")
print(expire(goods, 1))
