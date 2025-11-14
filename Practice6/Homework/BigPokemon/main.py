import requests


def get_pokemons():
    """
    Функция для получения всех покемонов

    :return pokemons [List]: Список покемонов
    """
    url = 'https://pokeapi.co/api/v2/pokemon?limit=500'
    response = requests.get(url)

    if response.status_code == 200:
        pokemons = response.json()
        return pokemons['results']
    else:
        return ('Ошибка!')

def poke_exist(name):
    """
    Функция для проверки существования покемона

    :param name [str]: Название покемона

    :return [bool]: Существует или нет
    """
    data_poke = get_pokemons()
    if name in [poke['name'] for poke in data_poke]:
        return True
    else:
        return False

def add_poke_to_team(name):
    """
    Функция для добавления покемона в команду (если его нет в команде)

    :param name[str]: Название покемона

    :return: Добавляет покемона в команду, если его в ней нет
            Выводит сообщение о результате
    """
    if poke_exist(name):
        if name not in poke_team:
            poke_team.append(name)
            print(f'{name} добавлен в команду!')
        else:
            print(f'{name} уже в команде!')
    else:
        print('Такого покемона не существует!')

def delete_poke_from_team(name):
    """
    Функция для удаления покемона из команды

    :param name [str]: Название покемона

    :return: Удаляет покемона из команды, если он там есть
    """
    if name in poke_team:
        poke_team.remove(name)
        print(f'{name} покинул команду!')
    else:
        print(f'{name} нет в команде!')

def get_info_team(poke_team):
    """
    Функция для вывода информации о покемонах в команде

    :param poke_team [List]: Список команды покемонов

    :return: Выводит информацию о покемонах в команде
    """
    url = 'https://pokeapi.co/api/v2/pokemon'

    print('\nПокемоны в команде:')
    if poke_team != []:
        for pokemon in poke_team:
            response_info_poke = requests.get(url + '/' + str(pokemon))
            if response_info_poke.status_code == 200:
                info = response_info_poke.json()
                count = 1
                print(f'\n{count}. ------------{info["name"]}------------')
                str_types = 'Тип: ' + ', '.join(type['type']['name'] for type in info['types'])
                print(str_types)
                print(f'Вес: {info["weight"]}')
                print(f'Рост: {info["height"]}')
                str_abil = 'Способности: ' + ', '.join(abil['ability']['name'] for abil in info['abilities'])
                print(str_abil)
                count += 1
    else:
        print('В команде нет покемонов!')

def get_info_poke(pokemon_name):
    """
    Функция для получения списка информации о конкретном покемоне

    :param pokemon_name [str]: Название покемона

    :return info [List]: Список с информацией о покемоне
    """
    url = 'https://pokeapi.co/api/v2/pokemon'
    response_info_poke = requests.get(url + '/' + str(pokemon_name))
    if response_info_poke.status_code == 200:
        info = response_info_poke.json()
        return info

def print_info_poke(pokemon_name):
    """
    Функция для вывода информации о покемоне

    :param pokemon_name [str]: Название покемона

    :return: Выводит информацию о покемоне
    """
    info = get_info_poke(pokemon_name)
    print(f'\nИнформация о: {info["name"]}')
    str_types = 'Тип: ' + ', '.join(type['type']['name'] for type in info['types'])
    print(str_types)
    print(f'Вес: {info["weight"]}')
    print(f'Рост: {info["height"]}')
    str_abil = 'Способности: ' + ', '.join(abil['ability']['name'] for abil in info['abilities'])
    print(str_abil)

def fight_pokemons(first_pokemon, second_pokemon):
    """
    Функция для тренировочного боя между двумя покемонами

    :param first_pokemon [str]: Название первого покемона
    :param second_pokemon [str]: Название второго покемона

    :return: Выводит сообщение с результатом боя
    """
    info_first = get_info_poke(first_pokemon)
    info_second = get_info_poke(second_pokemon)

    power_first = info_first['stats'][0]['base_stat']
    power_second = info_second['stats'][0]['base_stat']

    print(f'\nТренировочный бой: {first_pokemon} VS {second_pokemon}')
    if power_first > power_second:
        print(f'Победил - {first_pokemon}!')
    elif power_first < power_second:
        print(f'Победил - {second_pokemon}!')
    else:
        print('Ничья!')


poke_team = []
add_poke_to_team('clefairy')
get_info_team(poke_team)
print_info_poke('clefairy')
fight_pokemons('pidgey', 'clefairy')