from django.shortcuts import render
from home.forms import HomeForm
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
	template_name = 'home/home.html'

	def get(self,request):
		form = HomeForm()
		return render(request, self.template_name, {'form': form})


	def post(self, request):
	 	form = HomeForm(request.POST)
	 	if form.is_valid():
	 		text = form.cleaned_data['post']
	 	args = {'form': form, 'text': text}
	 	return render(request, self.template_name, args)
			

