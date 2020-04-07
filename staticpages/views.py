from django.views.generic import TemplateView


class HomeStaticpageView(TemplateView): 
    template_name = 'home.html'
