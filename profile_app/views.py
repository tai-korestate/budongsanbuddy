from django.shortcuts import render
from django.http import HttpResponseRedirect
from submit_site import models
from django.contrib.auth.models import User


# Create your views here.


def edit_profile(request):

    if not request.user.is_authenticated():
        return HttpRequestRedirect("/accounts")

    User.objects.all().filter(request.user.email)


def view_profile(request):


    if not request.user.is_authenticated():
        return HttpRequestRedirect("/accounts")



    user_info = (
            ("Email: ", request.user.email),
            ("??? ",request.user.username),
            ("Company:", request.user.first_name),
            ("Broker Name: ",request.user.last_name),
    )

    context = {
        "user_info":user_info
    }

    template = "profile_page.html"


    return render(request, template, context)
