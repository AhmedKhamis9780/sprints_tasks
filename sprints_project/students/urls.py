
from django.urls import path
from . import views
from .views import *
from .views import StudentUpdateView

urlpatterns = [
	path('Welcome/',views.Welcome,name='Welcome'),
    path('home/',views.home_view,name='home'),
	path('info/', StudentList.as_view()),
    path('list/',views.list_view,name='list'),
    path('create/', StudentCreate.as_view() ),
    path('<pk>/update', StudentUpdateView.as_view()),
    path('save/',views.list_save,name='save'),
    path('index/', views.home, name ='index')

]
