from django.shortcuts import render

def inicio(request):
    template="inicio.html"
    ctx={}
    return render(request, template, ctx)


def login(request):
    template="login.html"
    ctx={}
    return render(request, template, ctx)

def registrarse(request):
    template="registrarse.html"
    ctx={}
    return render(request, template, ctx)

def contacto(request):
    template="contacto.html"
    ctx={}
    return render(request, template, ctx)