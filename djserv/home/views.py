from django.shortcuts import render
#from home.forms import HomeForm
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'
'''
    def get(self,request):
    	form=HoneForm()
    	return render(request, self.template_name, {'form':form})
'''