from django.urls import path
from .views import HomeStaticpageView
from .views import AboutStaticpageView

urlpatterns = [ 
    path('about/', AboutStaticpageView.as_view(), name='about'),
    path('', HomeStaticpageView.as_view(), name='home'), 
]
