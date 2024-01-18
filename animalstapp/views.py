from django.shortcuts import render, redirect
from .models import Animals
from .forms import AnimalForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

def home(request):
    return render(request, 'base.html')

def animal_list(request):
    animals = Animals.objects.all()
    return render(request, 'animals/animal_list.html', {'animals': animals})

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'animals/save.html', {'form': form})

