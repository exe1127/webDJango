from django.shortcuts import render

def inicio(request):
    template="inicio.html"
    ctx={}
    return render(request, template, ctx)