from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.views import generic
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'index.html')