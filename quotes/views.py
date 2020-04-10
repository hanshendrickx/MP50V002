from django.views.generic import ListView

from .models import Quote

class QuoteListView(ListView): 
    model = Quote 
    template_name = 'quotes/quote_list.html'