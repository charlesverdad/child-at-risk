from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader


def home(request):
	return HttpResponse('Hello')

def home2(request):
	template = loader.get_template('children/hello.html')
	return HttpResponse(template.render(None, request))