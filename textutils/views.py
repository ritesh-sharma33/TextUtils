
# I have created this file - Ritesh

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#   return HttpResponse('''
#     <h1>Ritesh</h1> 
#     <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django CodeWithHarry</a>
#     ''')

# def about(request):
#   return HttpResponse('About Harry')

def index(request):
  #return HttpResponse("Home")
  return render(request, 'index.html')

def analyze(request):
  # Getting the text values
  djtext = request.GET.get('text', 'default')

  # Getting the checkbox values
  removepunc = request.GET.get('removepunc', 'off')
  fullcaps = request.GET.get('fullcaps', 'off')
  newlineremover = request.GET.get('newlineremover', 'off')
  spaceremover = request.GET.get('spaceremover', 'off')

  # Checking the checkbox on values
  if removepunc == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
      if char not in punctuations:
        analyzed = analyzed + char
    params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
  
  elif fullcaps == "on":
    analyzed = ""
    for char in djtext:
      analyzed = analyzed + char.upper()
    
    params = { 'purpose': 'Removed Punctuations', 'analyzed_text': analyzed }
    return render(request, 'analyze.html', params)

  elif newlineremover == "on":
    analyzed = ""
    for char in djtext:
      if char != "\n":
        analyzed = analyzed + char
    
    params = { 'purpose': 'Removed newlines', 'analyzed_text': analyzed }
    return render(request, 'analyze.html', params)

  elif spaceremover == "on":
    analyzed = ""
    for index, char in enumerate(djtext):
      if not(djtext[index] == " " and djtext[index+1] == " "):
        analyzed + analyzed + char
    
    params = { 'purpose': 'Removed Spaces', 'analyzed_text': analyzed }
    return render(request, 'analyze.html', params)

  else:
    return HttpResponse("Error")

def ex1(request):
  return HttpResponse("Exercise 1 - Solutions")