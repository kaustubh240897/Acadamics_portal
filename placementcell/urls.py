from django.conf.urls import url
from django.contrib import admin
from .views import home_page
from . import views
from .views import login_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home_page'),
    url(r'^Recruiter_register/$', views.Recruiter_registerView.as_view(), name='register'),
    url(r'^login/$', login_page, name='login'),
]
