# Django
from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [{
    'title':'Mont Blanc',
    'user':{
        'name': 'Andres',
        'picture':'https://picsum.photos/60/60/?image=1027',
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo':'https://picsum.photos/200/200/?image=1036',
    },
    {
    'title':'Via Lactea',
    'user':{
        'name': 'Christian van der Henst',
        'picture':'https://picsum.photos/60/60/?image=1005',
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo':'https://picsum.photos/200/200/?image=903',
    },
    {
    'title':'Nuevo Auditorio',
    'user':{
        'name': 'Uriel (thespianartist)',
        'picture':'https://picsum.photos/60/60/?image=883',
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo':'https://picsum.photos/200/200/?image=1076',
    },]

# Create your views here.
def list_posts(request):
    """List existing posts."""
    # content = []
    # for p in posts:
    #     content.append(
    #         """
    #         <p><strong>{name}</strong></p>
    #         <p><small>{age} - <i>{timestamp}</i></small></p>
    #         <figure><img src="{picture}"></figure>
    #         """.format(**p)
    #     )
    # return HttpResponse('<br>'.join(content))
    return render(request,'feed.html',{'posts':posts})