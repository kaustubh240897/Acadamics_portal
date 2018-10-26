from django.conf.urls import url

from . import views

app_name='recruiter'

urlpatterns = [
    #/recruiter/
    url(r'^$', views.IndexView.as_view(), name='semester'),
    #/recruiter/1/
    # url(r'^(?P<pk>[0-9]+)/$' ,views.DetailView.as_view(), name='material'),

    url(r'^sem1_courses/$', views.CourseView1.as_view(),name='sem1'),
    url(r'^sem2_courses/$', views.CourseView2.as_view(),name='sem2'),
    url(r'^sem3_courses/$', views.CourseView3.as_view(),name='sem3'),
    url(r'^sem4_courses/$', views.CourseView4.as_view(),name='sem4'),
    url(r'^sem5_courses/$', views.CourseView5.as_view(),name='sem5'),
    url(r'^sem6_courses/$', views.CourseView6.as_view(),name='sem6'),
    url(r'^sem7_courses/$', views.CourseView7.as_view(),name='sem7'),
    url(r'^sem8_courses/$', views.CourseView8.as_view(),name='sem8'),
    url(r'^sem1_courses/sem1_course1/$', views.Sem1_Course1,name='sem1_course1'),
    url(r'^sem1_courses/sem1_course2/$', views.Sem1_Course2,name='sem1_course2'),
    url(r'^sem1_courses/sem1_course3/$', views.Sem1_Course3,name='sem1_course3'),
    url(r'^sem1_courses/sem1_course4/$', views.Sem1_Course4,name='sem1_course4'),
    url(r'^sem1_courses/sem1_course5/$', views.Sem1_Course5,name='sem1_course5'),






]