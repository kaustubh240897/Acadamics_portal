from django.conf.urls import url

from . import views

app_name = 'recruiter'

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
    url(r'^sem2_courses/sem2_course1/$', views.Sem2_Course1,name='sem2_course1'),
    url(r'^sem2_courses/sem2_course2/$', views.Sem2_Course2,name='sem2_course2'),
    url(r'^sem2_courses/sem2_course3/$', views.Sem2_Course3,name='sem2_course3'),
    url(r'^sem2_courses/sem2_course4/$', views.Sem2_Course4,name='sem2_course4'),
    url(r'^sem2_courses/sem2_course5/$', views.Sem2_Course5,name='sem2_course5'),
    url(r'^sem3_courses/sem3_course1/$', views.Sem3_Course1,name='sem3_course1'),
    url(r'^sem3_courses/sem3_course2/$', views.Sem3_Course2,name='sem3_course2'),
    url(r'^sem3_courses/sem3_course3/$', views.Sem3_Course3,name='sem3_course3'),
    url(r'^sem3_courses/sem3_course4/$', views.Sem3_Course4,name='sem3_course4'),
    url(r'^sem3_courses/sem3_course5/$', views.Sem3_Course5,name='sem3_course5'),
    url(r'^sem4_courses/sem4_course1/$', views.Sem4_Course1,name='sem4_course1'),
    url(r'^sem4_courses/sem4_course2/$', views.Sem4_Course2,name='sem4_course2'),
    url(r'^sem4_courses/sem4_course3/$', views.Sem4_Course3,name='sem4_course3'),
    url(r'^sem4_courses/sem4_course4/$', views.Sem4_Course4,name='sem4_course4'),
    url(r'^sem4_courses/sem4_course5/$', views.Sem4_Course5,name='sem4_course5'),
    url(r'^sem5_courses/sem5_course1/$', views.Sem5_Course1,name='sem5_course1'),
    url(r'^sem5_courses/sem5_course2/$', views.Sem5_Course2,name='sem5_course2'),
    url(r'^sem5_courses/sem5_course3/$', views.Sem5_Course3,name='sem5_course3'),
    url(r'^sem5_courses/sem5_course4/$', views.Sem5_Course4,name='sem5_course4'),
    url(r'^sem5_courses/sem5_course5/$', views.Sem5_Course5,name='sem5_course5'),
    url(r'^sem6_courses/sem6_course1/$', views.Sem6_Course1,name='sem6_course1'),
    url(r'^sem6_courses/sem6_course2/$', views.Sem6_Course2,name='sem6_course2'),
    url(r'^sem6_courses/sem6_course3/$', views.Sem6_Course3,name='sem6_course3'),
    url(r'^sem6_courses/sem6_course4/$', views.Sem6_Course4,name='sem6_course4'),
    url(r'^sem6_courses/sem6_course5/$', views.Sem6_Course5,name='sem6_course5'),
    url(r'^sem7_courses/sem7_course1/$', views.Sem7_Course1,name='sem7_course1'),
    url(r'^sem7_courses/sem7_course2/$', views.Sem7_Course2,name='sem7_course2'),
    url(r'^sem7_courses/sem7_course3/$', views.Sem7_Course3,name='sem7_course3'),
    url(r'^sem7_courses/sem7_course4/$', views.Sem7_Course4,name='sem7_course4'),
    url(r'^sem7_courses/sem7_course5/$', views.Sem7_Course5,name='sem7_course5'),
    url(r'^sem8_courses/sem8_course1/$', views.Sem8_Course1,name='sem8_course1'),







]