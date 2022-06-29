from django.shortcuts import render, redirect
from django.http import HttpResponse
from ftsys.models import Item

def MainPage(request):
   # return render(request, 'mainpage.html', {
   # 'NewSurname':request.POST.get('Sname'),
   # 'NewFirstname':request.POST.get('Fname'),
   # 'NewMiddlename':request.POST.get('Mname'),
   # 'NewAge':request.POST.get('Age'),
   # 'NewAddress':request.POST.get('Address'),
   # 'NewContact':request.POST.get('Contact'),
   # 'NewDisease':request.POST.get('Dropdown'),
   # 'NewSpecify':request.POST.get('Specify'),
   # 'NewPlan':request.POST.get('Dropdown2'),
   # 'NewTotal':request.POST.get('Total'),
   # })
   if request.method == 'POST':
      Item.objects.create(sname=request.POST['Sname'],
         fname=request.POST['Fname'],
         mname=request.POST['Mname'],
         age=request.POST['Age'],
         add=request.POST['Address'],
         contact=request.POST['Contact'],
         disease=request.POST['Dropdown'],
         specifydisease=request.POST['Specify'],
         plan=request.POST['Dropdown2'],
         total=request.POST['Total'])
     #return HttpResponse(request.POST['fitness1'])
      return redirect ('/')
   storage=Item.objects.all()
   return render(request, 'mainpage.html',{'NewStorage':storage})

