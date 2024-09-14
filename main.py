from decimal import Decimal
from datetime import date, datetime, timedelta


def add(items: dict, title: str, amount: Decimal, expiration_date: str = None):
    if expiration_date:
        true_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        true_date = true_date.date()
    else:
        true_date = None
    item = {'amount': amount, 'expiration_date': true_date}
    if title in items:
        items[title].append(item)
    else:
        items[title] = [item]


def add_by_note(items: dict, note: str):
    split_note = note.split()
    if '-' in split_note[-1]:
        title = ' '.join(split_note[0: -2])
        add(items, title, Decimal(split_note[-2]), split_note[-1])
    else:
        title = ' '.join(split_note[0: -1])
        add(items, title, Decimal(split_note[-1]), None)


def find(items: dict, needle: str) -> list:
    found = []
    for item in items.keys():
        search = item.lower().find(needle.lower())
        if search != -1:
            found.append(item)
    return found


def amount(items: dict, needle: str) -> Decimal:
    found = Decimal("0")
    for key in items.keys():
        search = key.lower().find(needle.lower())
        if search != -1:
            for part in items[key]:
                found += Decimal(part['amount'])
    return found


def expire(items: dict, in_advance_days: int = 0) -> list[tuple]:
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
