from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Create your views here.
def home(request):
	return HttpResponse('game lobby')