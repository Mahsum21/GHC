from django import template
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

table = ""

def Index(request):
    context = {
    }
    return render(request,'connection/index.html',context)


def Horaires(request):
    context = {
    }
    return render(request,'connection/horaires.html',context)

def Admin(request):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/admin.html', context)

def Personne(request):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/classe/index.html', context)

def Operations(request, table, operation):
    context = {
        'operation' : operation,
        'table' : table, 
    }
    return render(request,'connection/classe/index.html',context)

