from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$",views.submit),
    url(r"^edit/$", views.edit_manager),
    url(r"^edit/page", views.edit_mode)
]




