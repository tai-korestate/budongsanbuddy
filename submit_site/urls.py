from django.conf.urls import url
from . import views


urlpatterns = [
    url("^$",views.submit),
    url("^edit", views.edit_manager),
    url(r"^edit/page", views.edit_mode)
]




