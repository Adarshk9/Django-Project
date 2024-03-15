#I have created this file - Adarsh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def removepunc(request):
    print(request.GET.get('text','nothing here'))
    return HttpResponse("Remove Punctuation")
def capitalizefirst(request):
    return HttpResponse("capitalize first letter")
def newlineremover(request):
    return HttpResponse("New Line Remover")
def spaceremover(request):
    return HttpResponse("Space Remover")
def charcount(request):
    return HttpResponse("character count")