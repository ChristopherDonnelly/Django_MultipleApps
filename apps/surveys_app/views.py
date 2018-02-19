from __future__ import unicode_literals 
 
from django.shortcuts import render, HttpResponse, redirect 
from django.utils.html import escape 
 
def index(request):
    response = "List all surveys here!"
    return HttpResponse(response)
    # return render(request, "surveys_app/index.html") 

def new(request):
    return render(request, "surveys_app/new.html") 

def process_form(request):

    try:
        request.session['counter'] += 1
    except:
        request.session['counter'] = 1
    
    request.session['full_name'] = request.POST['full_name']
    request.session['language'] = request.POST['location']
    request.session['location'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
   
    return redirect('/surveys/results/')

def results(request):
    context = {
        'name': request.session['full_name'],
        'language': request.session['location'],
        'location': request.session['language'],
        'comment': request.session['comment']
    }
        
    return render(request, "surveys_app/results.html", context)

def back(request):
    try:
        del request.session['full_name']
        del request.session['location']
        del request.session['language']
        del request.session['comment']
    except:
        pass

    return redirect('/surveys/new')