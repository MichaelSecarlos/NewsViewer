from django.shortcuts import render
from news.models import New

def home(request):
    noticias = New.objects.all()
    return render(request, 'index.html', {"news":noticias})