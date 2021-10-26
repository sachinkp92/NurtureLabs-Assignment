from django.urls import path, include
from.import views
from rest_framework import routers
from django.urls import path
from myapp.views import AdvisorList, AdvisorDetail, UserList, UserDetail, UserloginList, AdvisorbookList,AdvisorbookDetail


urlpatterns = [
    path('', views.index, name='index'),
    path('advisor/',AdvisorList.as_view()),
    path('advisor/<int:pk>/',AdvisorDetail.as_view()),
    path('user/register/',UserList.as_view()),
    path('user/register/<int:pk>/',UserDetail.as_view()),
    path('user/login/',UserloginList.as_view()),
    path('user/advisor/',AdvisorbookList.as_view()),
    path('user/advisor/<int:pk>/',AdvisorbookDetail.as_view()),

]
