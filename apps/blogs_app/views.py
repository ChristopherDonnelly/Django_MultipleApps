# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Blog

# the index function is called when root is visited
def index(request):
    response = "List all blogs here!"

    return render(request, "blogs_app/index.html")
    # return HttpResponse(response)

# the new function is called when new/ is visited
def new(request):
    response = "Create New Blog!"
    return HttpResponse(response)

# the create function is called when create/ is visited
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50

        try:
            print "Trying to assign"
            request.session['new'] += 1
        except:
            request.session['new'] = 1
            print 'Failed'

        return redirect("/")
    else:
        return redirect("/")

def update(request):
    errors = Blog.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        return redirect('/blogs')
        
# the show function is called in order to display a specific blog when a number [0-9] is passed
def show(request, blog_num):
    response = "Show Blog number {}".format(blog_num)
    return HttpResponse(response)

# the edit function is called in order to edit a specific blog when a number [0-9] is passed
def edit(request, blog_num):
    response = "Edit Blog number {}".format(blog_num)
    return HttpResponse(response)

# the destroy function is called in order to delete a specific blog when a number [0-9] is passed
def destroy(request, blog_num):
    # response = "Destroy Blog number {}".format(blog_num)
    return redirect('/')
