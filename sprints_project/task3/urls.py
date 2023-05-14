
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('task3/',views.info_view,name='info'),

]
