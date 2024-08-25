from django.shortcuts import render

def home(request):
    return render(request, 'portfolio_app/home.html')
