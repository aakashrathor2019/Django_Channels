from django.shortcuts import render



def home(request):
    return render(request, 'index.html')

def name(reques):
    return render(request, 'index.html')