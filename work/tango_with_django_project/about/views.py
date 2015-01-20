from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("This tutorial has been put togather by: Nicholas Saunderson, 2057559s")