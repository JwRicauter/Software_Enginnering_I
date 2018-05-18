from django.shortcuts import render
from django.views.generic import TemplateView
from acceso.models import Usuario
from .seguridad import Seguridad	

seguridad = Seguridad()

def sesion(request):

	context = {}

	context['error'] = False

	if request.method == 'POST':
		indicador = request.POST['indicador']
		if (indicador == 'login'):
			loginUser = request.POST['loginUser']
			loginPwd = request.POST['loginPwd']
			info = seguridad.ingresarUsuario(loginUser, loginPwd)

			# Verificar si el usuario aprobó los test de seguridad
			if info == True:
				context['success'] = "Conectado"
				return render(request, 'acceso/ok.html', context)
			else:
				context['error'] = True
				context['error_msg'] = info
				return render(request, 'acceso/sesion.html', context)
		
		elif (indicador == 'registro'):
			registroUser = request.POST['registroUser']
			registroPwd1 = request.POST['registroPwd1']
			registroPwd2 = request.POST['registroPwd2']

			info = seguridad.registrarUsuario(registroUser, registroPwd1, registroPwd2)

			if info == True:
				context['success'] = "Registrado"
				return render(request, 'acceso/ok.html', context)
			else:
				context['error'] = True
				context['error_msg_registro'] = info
				return render(request, 'acceso/sesion.html', context)

	return render(request, 'acceso/sesion.html', context)	