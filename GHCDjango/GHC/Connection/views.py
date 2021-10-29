from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Index(request):
	message = "<h1 style='text-align:center'> Bienvenue chez Mahsis</h1>"
	return HttpResponse(message)