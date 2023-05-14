
from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('Welcome/',views.Welcome,name='Welcome'),
	path('info/', StudentList.as_view()),
    path('list/',views.list_view,name='list'),

]
