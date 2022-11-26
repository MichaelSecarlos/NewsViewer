from django.shortcuts import render
from news.models import New
from news.forms import NewForm

# Create your views here.
def formView(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, "form.html", {})
