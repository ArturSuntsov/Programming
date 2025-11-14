from django.shortcuts import render
import requests


def list_breeds(request):
    """
    Показывает список всех пород собак

    Args:
        request: запрос от пользователя.

    Returns:
        Страницу с породами (или пустой список, если что-то пошло не так).
    """
    url = 'https://dog.ceo/api/breeds/list/all'
    response = requests.get(url)

    breeds = []
    if response.status_code == 200:
        data = response.json()
        breeds = list(data['message'].keys())

    return render(request, 'list_breeds.html', {'breeds': breeds})


def breeds_images(request):
    """
    Показывает картинки для выбранных пород.

    Args:
        request: запрос с параметром 'breeds' (породы через запятую).

    Returns:
        Страницу с картинками собак.
    """
    str_breeds = request.GET.get('breeds')
    if not str_breeds:
        return render(request, 'images_for_breeds.html', {'dogs_img': []})

    list_breeds = str_breeds.strip().split(',')
    dogs_img = []

    for breed in list_breeds:
        breed = breed.strip()
        if not breed:
            continue
        url = f'https://dog.ceo/api/breed/{breed}/images/random'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                dogs_img.append({
                    'breed': breed.title(),
                    'url_image': data['message']
                })

    return render(request, 'images_for_breeds.html', {'dogs_img': dogs_img})
