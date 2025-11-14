from django.shortcuts import render

# Create your views here.
def book_list(request):
    books = [
        {
            'title': 'book1',
            'author': 'author1',
            'year': '2001'
        },
        {
            'title': 'book2',
            'author': 'author2',
            'year': '2009'
        }
    ]

    return render(request, 'book_details.html', {'books': books})

