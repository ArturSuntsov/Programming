from django.shortcuts import render


def about(request):
    """Функция для рендеринга страницы о проекте"""
    return render(request, 'pages/about.html')


def rules(request):
    """Функция для рендеринга страницы правил"""
    return render(request, 'pages/rules.html')
