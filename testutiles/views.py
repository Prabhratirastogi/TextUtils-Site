from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

# def index(request):
#     return render(request,'home.html')

    
def analyze(request):
    
    #GET the text
    djtext =  request.POST.get('text','default')
    # check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    extraspaceremover= request.POST.get('extraspaceremover','off')
    charcounter= request.POST.get('charcounter','off')
    #check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext = analyzed
    if (fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to upper case','analyzed_text':analyzed}
        djtext = analyzed
    if (newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'removed new lines','analyzed_text':analyzed}
        djtext = analyzed
    if (extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed+char
        params = {'purpose':'Remove extra space','analyzed_text':analyzed}
        djtext = analyzed  
    if (charcounter == 'on'):
        analyzed = 0
        for char in djtext:
            if (char!= " "):
                analyzed = analyzed+1
        params = {'purpose':'Char Count','analyzed_text':analyzed}
        djtext = analyzed
    if (removepunc != 'on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on'and charcounter != 'on'):
        return render(request,'Error.html')
    return render(request,'analyze.html',params)
def home(request):
    return render(request,'home.html')
    
    