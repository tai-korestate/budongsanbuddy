from django.conf.urls import url
from . import views


urlpatterns = [
               url(r'^$', views.login_form),
               url(r'^login/',views.login_user),
               url(r'^logout/', views.logout_view),
               url(r'signup/', views.signup),
               url(r'^fail/', views.status),
]
