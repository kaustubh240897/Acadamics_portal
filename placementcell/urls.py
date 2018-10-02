from django.conf.urls import url
from django.contrib import admin
from .views import home_page
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
    url(r'^Recruiter_register/$', views.Recruiter_registerView.as_view(), name='register'),
]
