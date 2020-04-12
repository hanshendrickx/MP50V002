from django.views.generic import ListView, DetailView

from .models import Quote


class QuoteListView(ListView):
    model = Quote
    context_object_name = 'quote_list'
    template_name = 'quotes/quote_list.html'


class QuoteDetailView(DetailView): 
    model = Quote
    context_object_name = 'quote'
    template_name = 'quotes/quote_detail.html'