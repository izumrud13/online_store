from django.urls import path

from catalog.views import index, contacts, mailing

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('mailing/', mailing)
]