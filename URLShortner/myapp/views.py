from django.shortcuts import render, redirect
from .models import ShortModel
from .forms import UrlForm
from .shortner import short 
from rest_framework import viewsets
from myapp.serializers import UrlSerializer
# Create your views here.

def Home(request, token): # function to redirect to the original site using token
    long_url = ShortModel.objects.filter(short_url = token)[0]
    return redirect(long_url.long_url)


class UrlViewSet(viewsets.ModelViewSet): #
    queryset = ShortModel.objects.all() # showing all data in model 
    serializer_class = UrlSerializer


def Make(request): # function to validate and save the UrlForm in model
    form = UrlForm(request.POST)
    a = ""
    if request.method =="POST":
        if form.is_valid():
            NewUrl = form.save(commit = False) # if form is valid iy should save
            a = short().grant_token() # using grand_token function fron class short in shortner.py
            NewUrl.short_url = a
            NewUrl.save()
        else:                         # if form has erors or same url pushed again print invalid error
            form = UrlForm()
            a = "Invalid URL"
    return render (request, "home.html", {"form": form, "a":a})

 