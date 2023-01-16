from django.shortcuts import render
from django.contrib import messages
from routes.forms import RouteForm

def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})

def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        a = 1
        return render(request, 'routes/home.html', {'form': form})
    else:
        print(1)
        form = RouteForm()
        messages.error(request, 'Нет данных для поиска')
        return render(request, 'routes/home.html', {'form': form})