from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import info
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .forms import *

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

class StudentCreate(CreateView):
	# specify the model for create view
	model = info
	# specify the fields to be displayed
	fields = ['f_name', 'l_name']


class StudentUpdateView(UpdateView):
	# specify the model you want to use
	model = info
	# specify the fields
	fields = ["f_name","l_name"]
	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="/"

def home_view(request):
	
	# save the form data to model
	context ={}
	context['StudentForm']=StudentForm()
	return render(request,"home2.html",context)

def list_save(request):
	form = StudentForm(request.POST or None)
	print(form.is_valid())
	if form.is_valid():
		print('i am here')
		form.save()	
	else: HttpResponse("something wrong in entered data")	
	# context ={}
	# # add the dictionary during initialization
	# context["dataset"] = info.objects.all()
	return list_view(request)
	#return render(request, "list_view.html", context)	

def home(request):
	# check if the request is post
	if request.method =='POST':
		# Pass the form data to the form class
		details = PostForm(request.POST)
	# In the 'form' class the clean function
	# is defined, if all the data is correct
	# as per the clean function, it returns true
		if details.is_valid():
			# Temporarily make an object to be add some
			# logic into the data if there is such a need
			# before writing to the database
			post = details.save(commit = False)
			# Finally write the changes into database
			post.save()
			# redirect it to some another page indicating data
			# was inserted successfully
			return HttpResponse("data submitted successfully")
		else:
			# Redirect back to the same page if the data
			# was invalid
			return render(request, "home.html", {'form':details})
	else:	
		# If the request is a GET request then,
		# create an empty form object and
		# render it into the page
		form = PostForm(None)
		return render(request, 'home.html', {'form':form})