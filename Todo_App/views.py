from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tasks/list.html', context={'tasks': tasks, 'form': form})
