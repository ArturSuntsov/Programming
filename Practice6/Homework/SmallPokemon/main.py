import requests

# Получаем первые 20 покемонов.
url = 'https://pokeapi.co/api/v2/pokemon'
params = {'limit': 20}

response = requests.get(url, params=params)

# Если запрос прошёл успешно — выводим имена, иначе пишем "Ошибка!".
if response.status_code == 200:
    data = response.json()
    for pokemon in data['results']:
        print(pokemon['name'])
else:
    print('Ошибка!')

# Спрашиваем у пользователя имя покемона и ищем про него информацию.
pokemon_name = input('Введите название покемона:')
response_info = requests.get(url + '/' + str(pokemon_name))

# Если такой покемон есть — выводим его данные.
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
