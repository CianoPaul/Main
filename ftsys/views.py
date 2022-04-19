from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
   return render(request, 'mainpage.html', {
   'NewSurname':request.POST.get('fitness1'),})
   #if request.method == 'POST':
   #   return HttpResponse(request.POST['fitness1'])
   #return render(request, 'mainpage.html')
