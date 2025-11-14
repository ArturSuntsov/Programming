from django.shortcuts import render
import requests

# Create your views here.
def list_breeds(request):
    """
    Отображает страницу со списком всех пород собак

    param: request: http-запрос, отправленный пользователем

    return: list_breeds.html : Рендерит html страницу и передает туда список пород
    """
    url = 'https://dog.ceo/api/breeds/list/all'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        breeds = list(data['message'].keys())

        return render(request, 'list_breeds.html', {'breeds': breeds})

    return render(request, 'list_breeds.html')

def breeds_images(request):
    """
    Отображает страницу со списком всех пород собак

    param: request: http-запрос, отправленный пользователем

    return: list_breeds.html : Рендерит html страницу для картинок собак
            и передает туда список словарей { [порода: url-адрес картинки] }
    """
    str_breeds = request.GET.get('breeds')
    if not str_breeds:
        return render(request, 'images_for_breeds.html', {'dogs_img': []})

    list_breeds = (str_breeds.strip()).split(',')

    list_urls_breeds = []
    for breed in list_breeds:
        url = f'https://dog.ceo/api/breed/{breed}/images/random'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                list_urls_breeds.append(
                    {
                        'breed': breed.title(),
                        'url_image': data['message']
                    })
            else:
                print('Порода не найдена!')

    return render(request, 'images_for_breeds.html', {'dogs_img': list_urls_breeds})