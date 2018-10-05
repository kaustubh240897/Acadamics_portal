# from django.conf.urls import url
# from django.contrib import admin
# from .views import home_page
# from . import views
# from .views import login_page
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', home_page, name='home_page'),
#     url(r'^Recruiter_register/$', views.Recruiter_registerView.as_view(), name='register'),
#     url(r'^login/$', login_page, name='login'),
# ]
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="logout.html"), {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
]
