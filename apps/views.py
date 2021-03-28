from django.shortcuts import render, redirect, get_object_or_404

from .forms import AppForm
from .models import App

# Create your views here.
def index(request):
    apps = App.objects.all()
    context = {
        'apps': apps,
    }
    return render(request, 'apps/index.html', context)

def create(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apps:index')
    else:
        form = AppForm()
    context = {
        'form': form,
    }
    return render(request, 'apps/create.html', context)

def detail(request, *args, **kwargs):
    app = get_object_or_404(App, pk=kwargs.get('pk'))
    context = {
        'app': app,
    }
    return render(request, f'apps/{app.number}/index.html', context)

def delete(request, *args, **kwargs):
    app = get_object_or_404(App, pk=kwargs.get('pk'))
    app.delete()
    return redirect('apps:index')

def update(request, *args, **kwargs):
    app = get_object_or_404(App, pk=kwargs.get('pk'))
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES, instance=app)
        if form.is_valid():
            form.save()
            return redirect('apps:index')
    else:
        form = AppForm(instance=app)
    context = {
        'form': form,
    }
    return render(request, 'apps/create.html', context)
    