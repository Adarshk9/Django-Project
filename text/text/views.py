#I have created this file - Adarsh
from django.http import HttpResponse
def index(request):
    l = ['''Index Page<br>''','''Space Remover <a href="http://127.0.0.1:8000/spaceremove">Click here</a><br>'''
         '''Punctutation Remover <a href="http://127.0.0.1:8000/puncremove">Click here</a><br>'''
         '''Character Counter <a href="http://127.0.0.1:8000/charcount">Click here</a>'''
         ]
    return HttpResponse(l)
def spaceremove(request):
    return HttpResponse('''Space Remover<br> <a href="/">Click Here to Go back</a>''')
def puncremover(request):
    return HttpResponse('''Punctuation Remover<br> <a href="/">Click Here to Go back</a>''')
def charcount(request):
    return HttpResponse('''Character Counter<br> <a href="/">Click Here to Go back</a>''')

#from django.http import HttpResponse
#def index(request):
#   l = ['''<h2>Adarsh's top favourite sites</h2>'''
#        '''<h3>1. Youtube </h3><a href="https://www.youtube.com/">Click here to visit </a>''',
#         '''<h3>2. Google </h3><a href="https://www.google.com/">Click here to visit </a>'''
#         ]
#    return HttpResponse(l)
#def about(request):
#    return HttpResponse("about function executed!")
