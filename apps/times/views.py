from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
	current = {
		'time': datetime.datetime.now(),
	}
	return render(request, 'times/index.html', current)