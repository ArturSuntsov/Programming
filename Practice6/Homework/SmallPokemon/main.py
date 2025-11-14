import requests

# Вывод первых 20 покемонов
url = 'https://pokeapi.co/api/v2/pokemon'
params = {'limit': 20}

response = requests.get(url, params=params)

# Проверка на выполнение и вывод имен покемонов
if response.status_code == 200:
    data = response.json()
    for pokemon in data['results']:
        print(pokemon['name'])
else:
    print('Ошибка!')

# Отображение информации о введенном покемоне
pokemon_name = input('Введите название покемона:')
response_info = requests.get(url + '/' + str(pokemon_name))

#  Проверка на выполнение и вывод конкретных данных
if response_info.status_code == 200:
    data = response_info.json()
    print('Информация о покемоне:')
    print(f'Имя: {data["name"]}')
    str_types = 'Тип: ' + ', '.join(type['type']['name'] for type in data['types'])
    print(str_types)
    print(f'Вес: {data["weight"]}')
    print(f'Рост: {data["height"]}')
    str_abil = 'Способности: ' + ', '.join(abil['ability']['name'] for abil in data['abilities'])
    print(str_abil)