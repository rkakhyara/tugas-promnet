from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def education(request):
    return render(request,'education.html')

def experiences(request):
    return render(request,'experiences.html')

def project(request):
    return render(request,'project.html')