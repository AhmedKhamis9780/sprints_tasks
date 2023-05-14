from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import student,courses
from django.views.generic.list import ListView

def info_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}
	# add the dictionary during initialization
	context["student_info"] = student.objects.all() 
	context["courses_info"] = courses.objects.all()
	return render(request, "table.html", context)
# class StudentList(ListView):
# 	# specify the model for list view
# 	model = info