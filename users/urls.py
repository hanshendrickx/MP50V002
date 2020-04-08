# this files is obsolete because we have installed allauth
# for completeness we leave the code here, this file could be deleted
from django.urls import path
from .views import SignupPageView


urlpatterns = [ 
    path('signup/', SignupPageView.as_view(), name='signup'), 
]