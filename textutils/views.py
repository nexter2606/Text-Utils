#created by mee

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse('hello Dj')

def analyze(request):

    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    charcounter=request.GET.get('charcounter','off')
    smallcase=request.GET.get('smallcase','off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=""
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Upper Case-', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params) 

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!='\n':
                analyzed=analyzed + char
            
        params = {'purpose': 'New Line Remover-', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params) 

    elif(charcounter=="on"):
        analyzed = 0
        for char in djtext:
            if char!='\n':
                analyzed= analyzed + len(char)
            

        params = {'purpose': 'No. Characters in your Text are:', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)   


    elif(smallcase=="on"):
        analyzed = ""
        for char in djtext:
             analyzed=analyzed + char.lower()
            
        params = {'purpose': 'small case-', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)                    


    else:
        return HttpResponse('Error')