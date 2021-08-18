from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.send_msg)
]