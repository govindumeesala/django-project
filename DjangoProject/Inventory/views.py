from django.shortcuts import render, redirect
from .forms import *
from .models import *
  
# Create your views here.
 
def HomePage(request):
    context = {
        "name": "Govindu",
        "role": "user",
        "numbers": [1,2,3,4,5,6]
    }
    return render(request, 'home.html', context)

def LoginPage(request):
    return render(request, "login.html")

def ContactPage(request):
    return render(request, "contact.html")

def ServicePage(request):
    return render(request, "service.html")

def  Interns_add_page(request):
    context={
        'interns_form':Interns_form()
    }
    if request.method == "POST":
        interns_form = Interns_form(request.POST)
        if interns_form.is_valid():
            interns_form.save()

    return render(request,'interns.html',context)

def Interns_details(request):
    interns_details = Interns.objects.all()

    return render(request, 'interns_details.html', {'interns_details': interns_details})

def Delete_intern(request, id):
    selected_intern = Interns.objects.get(id=id)
    selected_intern.delete()
    return redirect('/inventory/interns/')

def Update_intern(request, id):
    selected_intern = Interns.objects.get(id=id)

    context = {
        'interns_form' : Interns_form(instance=selected_intern)
    }
    if(request.method=="POST"):
        intern_form=Interns_form(request.POST,instance=selected_intern)
        if(intern_form.is_valid()):
            intern_form.save()
            return redirect('/inventory/interns/')

    return render(request,'interns.html',context)
