from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_mascota(request):
    return HttpResponse('estou na view de mascota')