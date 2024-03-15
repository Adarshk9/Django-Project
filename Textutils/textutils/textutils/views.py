#I have created this file - Adarsh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.GET.get('text','nothing here')
    removepunc = request.GET.get('removepunc','off')
    capitalize = request.GET.get('allcaps','off')
    charactercount = request.GET.get('charcount','off')
    wordcountt = request.GET.get('wordcount','off')
    print(djtext)
    print(removepunc)
    if(removepunc=='on'):
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed+=i
        params = {'purpose':'Remove Punctuation', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    elif(capitalize=='on'):
        analyzed = ""
        for i in djtext:
            analyzed+=i.upper()
        params = {'purpose':'Capitalise All','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(charactercount=='on'):
        analyze = 0
        for i in djtext:
            if(i!=' '):
                analyze+=1
        params = {'purpose':'Character Count','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    elif(wordcountt=='on'):
        analyze = 1
        for i in djtext:
            if(i==' '):
                analyze+=1
        params = {'purpose':'Word Counting','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Invalid choice \n An Error Occured")
