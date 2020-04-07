from django.urls import path
from .views import HomeStaticpageView

urlpatterns = [ 
    path('', HomeStaticpageView.as_view(), name='home'), 
]
