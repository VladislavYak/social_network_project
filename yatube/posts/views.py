from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('foobar')

def group_posts(request, slug):
    return HttpResponse(f'barfoo + {slug}')