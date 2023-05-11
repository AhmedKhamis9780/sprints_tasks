from django.http import HttpResponse
from django.template import loader

def portofolio(request):
	template = loader.get_template('cv.html')
	return HttpResponse(template.render())	
