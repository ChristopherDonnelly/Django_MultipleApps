from __future__ import unicode_literals 
 
from django.shortcuts import render, HttpResponse, redirect 
from django.utils.html import escape 
 
def register(request): 
    response = "Register here!"
    return HttpResponse(response)

def login(request): 
    response = "Login here!"
    return HttpResponse(response)

def users(request): 
    response = "List all Users here!"
    return HttpResponse(response)

def new(request): 
    response = "Create New User here!"
    return HttpResponse(response)

