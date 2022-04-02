from django.shortcuts import render
#from django.http import HttpResponse

def MainPage(request):
   return render(request, 'mainpage.html') #eto ang babaguhin fitnesstalk1.html for example
