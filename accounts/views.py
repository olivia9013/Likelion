from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("accounts")

# Create your views here.
