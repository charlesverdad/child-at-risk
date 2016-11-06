from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader


def home(request):
	template = loader.get_template('children/index.html')
	return HttpResponse(template.render(None, request))

def childprofile(request):
	template = loader.get_template('children/child-profile.html')
	return HttpResponse(template.render(None, request))