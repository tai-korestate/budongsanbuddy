from django.contrib.auth.models import User
from hashlib import sha256
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/submit")

    status = ''

    try:
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
   
    except ValueError:
        return HttpResponseRedirect("/accounts/fail?err=Please fill out all fields.")
    except NameError:
        return HttpResponseRedirect("/accounts/fail?err=That username or email has already been registered.")

    except:
        return HttpResponseRedirect("/accounts/fail?err=UserName already in use.")
 
    template = "signup.html"
    context = {"welcome":"welcome",
               "status":"status"
               }
               
    return render(request, template, context)


def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/submit')

    template = "accounts.html"
    context = {'welcome':'welcome'}
    return render(request, template, context)


def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/submit')

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
            return HttpResponse("/fail?err=Disabled Account")

    else:
        status = "Invalid Sign in"
        return HttpResponseRedirect("/accounts/fail?err=Invalid Login: Please fillout all fields")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accounts")


def status(request):

    if request.GET:
        status = "Error: %s" % request.GET['err']
    else:
        status = "Error 404"

    template = "status.html"
    context = {"status_message" : status}

    return render(request, template, context) 
