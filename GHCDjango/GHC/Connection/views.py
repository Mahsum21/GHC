from django import template
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def Index(request):
	# message = "<h1 style='text-align:center'> Bienvenue chez Mahsis</h1>"
	template = loader.get_template('connection/index.html')
	return HttpResponse(template.render(request=request))


def Horaires(request):
	# message = "<h1 style='text-align:center'> Bienvenue chez Mahsis</h1>"
	template = loader.get_template('connection/horaires.html')
	return HttpResponse(template.render(request=request))


def Admin(request):
	# message = "<h1 style='text-align:center'> Bienvenue chez Mahsis</h1>"
	template = loader.get_template('connection/admin.html')
	return HttpResponse(template.render(request=request))