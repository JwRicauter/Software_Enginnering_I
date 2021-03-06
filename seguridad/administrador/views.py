from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Sesion(TemplateView):
    template_name = "acceso/sesion.html"

	def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context