from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'portfolio/index.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def greet_by_name(request, name):
    context = {'name' : name}
    return render(request, 'portfolio/greet.html', context)