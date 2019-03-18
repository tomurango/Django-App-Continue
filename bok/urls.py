from django.urls import path
from . import views

urlpatterns = [
    path('mybok', views.mybok, name='mybok'),
    path('', views.home, name='home'),
    path('priv', views.private_page, name='priv'),
    path('pub', views.public_page, name='pub'),
    path('signup',views.sign_up,name='signup'),
    path('job',views.job_des, name='job'),
    path('task',views.task, name='task'),
    path('jobname',views.job_name,name='jobname'),
    path('jobchange',views.job_change,name='jobchange'),
    path('skill',views.skill,name='skill')
]