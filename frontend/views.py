from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')

def terms(request):
    return render(request, 'frontend/terms.html')

def contact(request):
    return render(request, 'frontend/contact.html')
