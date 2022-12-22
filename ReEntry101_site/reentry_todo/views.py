from django.shortcuts import render

from django.views import View

# Create your views here.

class HomeView (View): 
    def get (self, request):
        return render(request=request, template_name='index.html')
        