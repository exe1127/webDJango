from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import Registrarse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Usuario


def registrarse(request):

    if request.method == 'POST':
        form = Registrarse(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = Registrarse()
    return render(request, 'usuarios/registrarse.html', {'form': form})


def login(request):

    return render(request, 'usuarios/login.html')



