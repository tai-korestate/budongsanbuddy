from django.contrib.auth.models import User
from hashlib import sha1
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def signup(request):
    status = ''
    if request.method == 'POST':
            u_data = request.POST   
            user_creator = User.objects.create_user(
                     username = u_data['email'],
                     email =  u_data['email'],
                     password =  u_data['drwsp'],
                     first_name =  u_data['co_name'],
                     last_name =  u_data['phone_num'],
                     )
            user_creator.save()
            status = "Submission Complete"
            return HttpResponseRedirect("/submit")
    
    template = "signup.html"
    context = {"welcome":"welcome",
               "status":"status"
               }
    return render(request, template, context)


def login_form(request):
    template = "accounts.html"
    context = {'welcome':'welcome'}
    return render(request, template, context)


def login_user(request):
    status = "Unknown"
 
    try:
        username = request.POST['email'] #Add Filtering here
    except: 
        status = "problem with username"    
        
    try:
        password = request.POST['password'] #Add Filtering here
   
    except:
        status = "problem with username"    
    
    status = "Problem with auth"
    user = authenticate(username = username, password = password)
   
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect('/submit')
        else:
            return HttpResponse("Disabled Account")

    else:
        status = "Invalid Sign in"
        return HttpResponse("Invalid Login: %s" % status)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accounts") 
