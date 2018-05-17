from django.shortcuts import render
from django.views.generic import TemplateView
from acceso.models import Usuario

# Create your views here.

class Sesion(TemplateView):
	template_name = "acceso/sesion.html"

	def post(self, request, *args, **kwargs):
		form = self.login(request.POST)
		if form.is_valid():
			username = request.POST.get("correoUser", "")
			print(username)
			print("kajsnka")