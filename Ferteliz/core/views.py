
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm

def home (request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'core/register.html', {'form': form})
