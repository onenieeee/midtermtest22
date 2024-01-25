from django.shortcuts import render, redirect
from .models import Movies
from .forms import MoviesForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

def home(request):
    return render(request, 'base.html')

def animal_list(request):
    animals = Movies.objects.all()
    return render(request, 'movies/movies_list.html', {'movies': animals})

def add_animal(request):
    if request.method == 'POST':
        form = MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = MoviesForm()
    return render(request, 'animals/save.html', {'form': form})
# def search(request):
#     if request.method == "POST":
#         txt = request.POST['txtsearch']
#         table = Animals.objects.filter(name__icontains=txt)
#         context = {'pd': table}
#     return render(request, 'result.html', context)

def search_view(request):
    query = request.GET.get('q')
    if query:
        # Perform the search using the query
        animals = Movies.objects.filter(name__icontains=query)
    else:
        # If no query is provided, display all animals
        animals = Movies.objects.all()

    return render(request, 'animals/animal_list.html', {'animals': animals})
