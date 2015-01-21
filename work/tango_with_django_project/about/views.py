from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':"This tutorial has been put togather by: Nicholas Saunderson, 2057559s"}

    return render(request, 'rango/about.html', context_dict)