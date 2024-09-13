from decimal import Decimal
from datetime import date, datetime


def add(items: dict, title: str, amount: Decimal, expiration_date: str = None):
    true_date = datetime.strptime(expiration_date, "%Y-%m-%d")
    item = {'amount': amount, 'expiration_date': true_date.date()}
    if title in items:
        items[title].append(item)
    else:
        items[title] = [item]


def add_by_note(items: dict, note: str):
    split_note = note.split()
    title = split_note[0]
    title_counter = 0
    for part in split_note[1::]:
        if part.isdigit():
            break
        else:
            title += f" {part}"
            title_counter += 1
    add(items, title, Decimal(split_note[-2]), split_note[-1])


def find(items: dict, needle):
    ...


def amount(items: dict, needle):
    ...


def expire(items: dict, in_advance_days=0):
    ...


# Test part
goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': date(2023, 9, 30)}
    ]
}
add_by_note(goods, "Яйца Гусиные 4 2023-07-15 ")
print(goods)
