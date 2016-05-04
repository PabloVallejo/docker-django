from django.views.generic import TemplateView

class HomeView(TemplateView):
	""" Simple principal view.
	"""
	template_name = 'home.html'
