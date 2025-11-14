import requests

poke_team = []


def get_pokemons():
    """
    Получает список покемонов из API.

    Returns:
        Список покемонов или сообщение об ошибке.
    """
    url = 'https://pokeapi.co/api/v2/pokemon?limit=500'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['results']
    else:
        return 'Ошибка!'


def poke_exist(name):
    """
    Проверяет, существует ли покемон с таким именем.

    Args:
        name (str): Имя покемона.

    Returns:
        bool: True, если покемон существует, иначе False.
    """
    pokemons = get_pokemons()
    return name in [poke['name'] for poke in pokemons]


def add_poke_to_team(name):
    """
    Добавляет покемона в команду, если его там ещё нет.

    Args:
        name (str): Имя покемона.

    Returns:
        Ничего не возвращает, просто печатает результат.
    """
    if not poke_exist(name):
        print('Такого покемона не существует!')
        return

    if name in poke_team:
        print(f'{name} уже в команде!')
    else:
        poke_team.append(name)
        print(f'{name} добавлен в команду!')


def delete_poke_from_team(name):
    """
    Удаляет покемона из команды.

    Args:
        name (str): Имя покемона.

    Returns:
        Ничего не возвращает, просто печатает результат.
    """
    if name in poke_team:
        poke_team.remove(name)
        print(f'{name} покинул команду!')
    else:
        print(f'{name} нет в команде!')


def get_info_team(poke_team):
    """
    Выводит информацию обо всех покемонах в команде.

    Args:
        poke_team (list): Список имён покемонов.

    Returns:
        Ничего не возвращает, печатает данные.
    """
    print('\nПокемоны в команде:')
    if not poke_team:
        print('В команде нет покемонов!')
        return

    count = 1
    for name in poke_team:
        info = get_info_poke(name)
        if info:
            print(f'\n{count}. ------------{info["name"]}------------')
            types = ', '.join(t['type']['name'] for t in info['types'])
            print(f'Тип: {types}')
            print(f'Вес: {info["weight"]}')
            print(f'Рост: {info["height"]}')
            abilities = ', '.join(a['ability']['name'] for a in info['abilities'])
            print(f'Способности: {abilities}')
            count += 1


def get_info_poke(pokemon_name):
    """
    Получает полные данные о покемоне из API.

    Args:
        pokemon_name (str): Имя покемона.

    Returns:
        dict: Данные о покемоне или None, если ошибка.
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def print_info_poke(pokemon_name):
    """
    Печатает информацию о конкретном покемоне.

    Args:
        pokemon_name (str): Имя покемона.

    Returns:
        Ничего не возвращает, просто выводит данные.
    """
    info = get_info_poke(pokemon_name)
    if not info:
        print('Не удалось получить данные о покемоне.')
        return

    print(f'\nИнформация о: {info["name"]}')
    types = ', '.join(t['type']['name'] for t in info['types'])
    print(f'Тип: {types}')
    print(f'Вес: {info["weight"]}')
    print(f'Рост: {info["height"]}')
    abilities = ', '.join(a['ability']['name'] for a in info['abilities'])
    print(f'Способности: {abilities}')


def fight_pokemons(first_pokemon, second_pokemon):
    """
    Устраивает бой между двумя покемонами (по базовому здоровью).

    Args:
        first_pokemon (str): Имя первого покемона.
        second_pokemon (str): Имя второго покемона.

    Returns:
        Ничего не возвращает, печатает результат боя.
    """
    info1 = get_info_poke(first_pokemon)
    info2 = get_info_poke(second_pokemon)

    if not info1 or not info2:
        print('Один из покемонов не найден.')
        return

    hp1 = info1['stats'][0]['base_stat']
    hp2 = info2['stats'][0]['base_stat']

    print(f'\nТренировочный бой: {first_pokemon} VS {second_pokemon}')
    if hp1 > hp2:
        print(f'Победил — {first_pokemon}!')
    elif hp2 > hp1:
        print(f'Победил — {second_pokemon}!')
    else:
        print('Ничья!')


# Пример использования:
add_poke_to_team('clefairy')
get_info_team(poke_team)
print_info_poke('clefairy')
fight_pokemons('pidgey', 'clefairy')
