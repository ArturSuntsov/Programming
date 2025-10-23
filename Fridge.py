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

DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None):
    """
    Добавляет продукт (его название,его количество, 
    его срок годности).
    Args:
        items({}): словарь для добавления продуктов
        title(str): название продукта
        amount(Decimal): количество продукта
        expiration_date: срок годности
    Returns:
        Добавление элементов в словарь
    """
    if title not in items:
        items[title] = []
    properties = dict(amount=amount, expiration_date=expiration_date)
    if expiration_date:
        properties['expiration_date'] = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    items[title].append(properties)

def add_by_note(items, note):
    """
    Автоматически вызывает add,
    извлекает название, количество
    продукта из строки.
    Args:
        items({}): словарь для добавления продуктов
        note(str): строка с информацией о продукте
    Returns:
        Вызов функции add, извлечение информации о продукте
    """
    parts = str.split(note)
    
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
    Args:
        items({}): словарь с продуктами
        needle(str): искомый продукт
    Returns:
        list: Список искомых продуктов
    """
    result = []   
    
    for title in items:  
        if needle.lower() in title.lower(): 
            result.append(title)  
    return result



def amount(items, needle):
    """
    Считает общее количество продукта.
    
    Args:
        items({}): словарь с продуктами
        needle(str): название продукта для подсчета
    Returns:
        Decimal: общее количество продукта
    """
    matching_titles = find(items, needle)
    result = Decimal('0')

    for title in matching_titles:
        for properties in items[title]:
            result += properties['amount']
    return result
