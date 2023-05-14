from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import info
from django.views.generic.list import ListView
def Welcome(request):
	template = loader.get_template('show.html')
	return HttpResponse(template.render())
def list_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}
	# add the dictionary during initialization
	context["dataset"] = info.objects.all()
	return render(request, "list_view.html", context)
class StudentList(ListView):
	# specify the model for list view
	model = info