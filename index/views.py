from django.shortcuts import render

def home(request):
    return render(request, 'home-2.html', {})
