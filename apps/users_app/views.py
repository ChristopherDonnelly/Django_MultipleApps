from __future__ import unicode_literals 
 
from django.shortcuts import render, HttpResponse, redirect 
from django.utils.html import escape
from django.contrib import messages
from .models import User
 
def users(request): 
    return render(request, "users_app/index.html", { 'users': User.objects.all() })

def register(request): 
    response = "Register here!"
    return HttpResponse(response)

def login(request): 
    response = "Login here!"
    return HttpResponse(response)

def new(request):
    return render(request, "users_app/new.html")

def update(request, user_num):
    errors = User.objects.basic_validator(request.POST)
    goto = '/users'

    print "Update User Number: "+user_num

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)

        goto = '/users/{}/edit/'.format(user_num)
    else:
        try:
            user = User.objects.get(id = user_num)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
        except:
            pass

    return redirect(goto)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    goto = '/users'

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)

        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']

        goto = '/users/new/'
    else:
        try:
            print request.POST['first_name']
            print request.POST['last_name']
            print request.POST['email']

            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], age = 0)

            del request.session['first_name']
            del request.session['last_name']
            del request.session['email']
        except:
            pass

    return redirect(goto)

def show(request, user_num):
    return render(request, "users_app/show.html", { 'user': User.objects.get(id=user_num) })

def edit(request, user_num):
    return render(request, "users_app/edit.html", { 'user': User.objects.get(id=user_num) })

def destroy(request, user_num):
    exists = User.objects.filter(id=user_num).count()
    if exists:
        User.objects.get(id=user_num).delete()
    return redirect('/users')
