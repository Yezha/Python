from django.shortcuts import render
from .models import News

news = [
    {
        'title': 'Моя первая запись',
        'text': 'Большой текст для записи',
        'date': '17.01.2019',
        'avtor':'Ержан'
    },
    {
        'title': 'Моя вторая запись',
        'text': 'Большой текст для второй записи',
        'date': '20.01.2019',
        
    }
    
]

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request, 'blog/home.html', data)

def contacty(request):
    return render(request, 'blog/contacty.html', {'title': 'Страничка про нас'})
