from django.urls import path

from .views import QuoteListView, QuoteDetailView

urlpatterns = [
    path('', QuoteListView.as_view(), name='quote_list'),
    path('<uuid:pk>', QuoteDetailView.as_view(), name='quote_detail'),
]