import datetime
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

def add(items, title, amount, expiration_date=None):
    """
    Добавляет продукт (его название,его количество, 
    его срок годности).
    """
    if isinstance(amount, Decimal):
        amount_decimal = amount
    else:
        amount_decimal = Decimal(str(amount))
    
    date_obj = None
    if expiration_date is not None:
        if isinstance(expiration_date, str):
            date_obj = datetime.date.fromisoformat(expiration_date)
        else:
            date_obj = expiration_date
    
    if title not in items:
        items[title] = []
    
    items[title].append({
        'amount': amount_decimal,
        'expiration_date': date_obj
    })


def add_by_note(items, note):
    """
    Автоматически вызывает add,
    извлекает название, количество,
    продукта из строки.
    """
    parts = note.split() 
    
    if '-' in parts[-1]:
        expiration_date = parts[-1]
        amount = Decimal(parts[-2])
        product_name = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = Decimal(parts[-1])
        product_name = ' '.join(parts[:-1])
    
    add(items, product_name, amount, expiration_date)

def find(items, needle):
    """
    Ищет все продукты с заданным названием.
    """
    results = []
    needle_lower = needle.lower()
    for title in items:
        if needle_lower in title.lower():
            results.append(title)
    return results
    add(items, title, amount, expiration_date)


def amount(items, needle):
    """
    Считает общее количество продукта.
    """
    total = Decimal('0')
    
    if not items:
        return Decimal('0')
    
    for product_name in items:
        if needle.lower() in product_name.lower():
            for batch in items[product_name]:  
                total += batch['amount']  
    
    return total

