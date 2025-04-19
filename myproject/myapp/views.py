from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def boat(request):
    return render(request, 'boat.html')