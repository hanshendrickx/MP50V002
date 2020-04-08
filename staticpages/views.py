from django.views.generic import TemplateView


class HomeStaticpageView(TemplateView): 
    template_name = 'home.html'

class AboutStaticpageView(TemplateView): # new 
    template_name = 'about.html'    
