from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.conf import settings
import json
import requests

def home(request):
    return render(request, "home.html", {settings.BASE_URL})

# def home(request):
#     return render(request, "home.html", {settings.BASE_URL})
