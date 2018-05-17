from django.shortcuts import render
from django.views.generic import TemplateView
from acceso.models import Usuario

# Create your views here.

def sesion(request):
	print(request.method)
	if request.method == 'GET':
		print("askjdn")
		status = request.GET.get('correoUser')
		print(status)

	return render(request, 'acceso/sesion.html')	