from django.http import HttpResponse
from django.template import loader
def Welcome(request):
	template = loader.get_template('show.html')
	return HttpResponse(template.render())

