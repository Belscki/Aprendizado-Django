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
        'content': 'lorem aoçisdhasioçkndaikoçsndioçaksndikoç',
        'data' : 'Ontem'
    },
    {
        'author': 'Florinda',
        'title': 'Terceiro Post',
        'content': 'lorem aolskdjnaoçiklsdnaoçiknd ioahnsdioasniko noaiknjd ikoansdklo an',
        'data' : 'Ante-ontem'
    }
]

links =[
    {
        'video' : 'https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&si=CM0zas3kZVLRh7Yk'
    },
    {
        'video' : 'https://www.youtube.com/live/c0x_AaPjNCY?si=zFmm318lPWe6Mctk'
    },
    {
        'video' : 'https://youtu.be/s7aINQPGNDM?si=XPcy-ZqNWs0o5Cil'
    },
    {
        'video' : 'https://youtu.be/fHpiwPcTcYw?si=xHWe-tzUaehI6p4h'
    },
    {
        'video' : 'https://youtu.be/i5JykvxUk_A?si=iCHTNB71AojqNLQS'
    },
    {
        'video' : 'https://youtu.be/JIFqqdRxmVo?si=CyAvsYpZ8VzLAMu1'
    },
    {
        'video' : 'https://youtu.be/tujhGdn1EMI?si=VWmWfpxKgJ3rfuQB'
    },
    {
        'video' : 'https://youtu.be/c708Nf0cHrs?si=lOCn05mWkl7bO6j6'
    },
    {
        'video' : 'https://youtube.com/playlist?list=PLsTx8TSx2fHY01FnuxBdwiBiOdZdPGik7&si=jkfJqIZs1VWYatvA'
    },
    {
        'video' : 'https://youtu.be/pvh_UPHuz9U?si=DXYBej9uNbhTMp5c'
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

