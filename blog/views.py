from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Arthur',
        'title': 'Primeiro Post',
        'content': 'Claramente esse é o primeiro post',
        'data' : 'Hoje'
    },
    {
        'author': 'Madruga',
        'title': 'Segundo Post',
        'content': 'Claramente esse é não é o primeiro post',
        'data' : 'Ontem'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
# Create your views here.

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

