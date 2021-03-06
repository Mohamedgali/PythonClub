from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
    path('meetings/', views.meetings, name='meetings'),
    path('resources/', views.resources, name='resources'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('newresource/', views.newResource, name='newresource'),  

] 

