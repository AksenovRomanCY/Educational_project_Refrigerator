from decimal import Decimal
from datetime import date, datetime, timedelta


def add(items: dict, title: str, amount: Decimal, expiration_date: str = None):
    if expiration_date:
        true_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        true_date.date()
    else:
        true_date = None
    item = {'amount': amount, 'expiration_date': true_date}
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


def find(items: dict, needle: str):
    found = []
    for item in items.keys():
        search = item.lower().find(needle.lower())
        if search != -1:
            found.append(item)
    return found


def amount(items: dict, needle: str):
    found = 0
    for key in items.keys():
        search = key.lower().find(needle.lower())
        if search != -1:
            for part in items[key]:
                found += part['amount']
    return found


def expire(items: dict, in_advance_days: int = 0):
    found = []
    for key, item in items.items():
        for part in item:
            check_box = 1
            if isinstance(part['expiration_date'], datetime):
                expiration_date = part['expiration_date'].date()
            else:
                expiration_date = part['expiration_date']
            if part['expiration_date'] and expiration_date <= date.today() + timedelta(days=in_advance_days):
                for counter in range(len(found)):
                    if found[counter][0] == str(key):
                        update_good = (found[counter][0], found[counter][1]+part['amount'])
                        found.pop(counter)
                        found.append(update_good)
                        check_box = 0
                        break
                if check_box:
                    found.append((str(key), part['amount']))
    return found


# Test part
goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': date(2023, 9, 30)}
    ]
}
add(goods, 'Вода', Decimal('2.5'))
add_by_note(goods, "Яйца Гусиные 4 2023-07-15 ")
add_by_note(goods, "Яйца Гусиные 5 2025-07-17 ")
add_by_note(goods, "Яйца Гусиные 2 2025-10-17 ")
print(goods)

print(find(goods, "ца"))
print(amount(goods, "ца"))
print(expire(goods, 1))
