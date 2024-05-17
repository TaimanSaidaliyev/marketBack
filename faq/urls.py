from django.urls import path

from .views import *

urlpatterns = [
    path('list/', FAQList.as_view(),),
    path('contact_form/add/', FAQContactForm.as_view(),),
]