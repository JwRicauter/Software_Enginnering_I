from django.shortcuts import render
from django.views.generic import TemplateView
from acceso.models import Usuario


# Create your views here.

def sesion(request):



	if request.method == 'POST':
		indicador = request.POST['indicador']
		if (indicador == 'login'):
			loginUser = request.POST['loginUser']
			loginPwd = request.POST['loginPwd']
		elif (indicador == 'registro'):
			registroUser = request.POST['registroUser']
			registroPwd1 = request.POST['registroPwd1']
			registroPwd2 = request.POST['registroPwd2']
		

	return render(request, 'acceso/sesion.html')	