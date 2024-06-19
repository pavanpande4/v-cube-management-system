from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showPage(request):
    return render(request,'Base.html')

def loginpage(request):
    return render(request,'login.html')

def registerpage(request):
    return render(request,'register.html')