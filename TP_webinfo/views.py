from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
def index(request):
    return render(request,"index.html",{})
